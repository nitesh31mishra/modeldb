package ai.verta.modeldb.common.artifactStore.storageservice.s3;

import ai.verta.modeldb.common.CommonUtils;
import ai.verta.modeldb.common.config.S3Config;
import ai.verta.modeldb.common.exceptions.ModelDBException;
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.*;
import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import java.io.IOException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

// S3Client provides a wrapper to the regular AmazonS3 object. The goal is to ensure that the
// AmazonS3 object is
// _always_ valid when performing operations. If it is not, then that's a bug. This simplifies the
// handling of the API
// calls so that we don't have to keep worrying about refreshing the credentials on every call.
// We use a reference counter to keep track of when we have to shutdown a previous client that
// should not be used anymore.
public class S3Client {
  // AWS Releated Constants
  public static final String AWS_ROLE_ARN = "AWS_ROLE_ARN";
  public static final String AWS_WEB_IDENTITY_TOKEN_FILE = "AWS_WEB_IDENTITY_TOKEN_FILE";
  private static final Logger LOGGER = LogManager.getLogger(S3Service.class);

  private final String bucketName;

  private volatile AmazonS3 s3Client;
  private volatile AtomicInteger referenceCounter;
  private volatile AWSCredentials awsCredentials;

  public S3Client(S3Config s3Config) throws IOException, ModelDBException {
    String cloudAccessKey = s3Config.getCloudAccessKey();
    String cloudSecretKey = s3Config.getCloudSecretKey();
    String minioEndpoint = s3Config.getMinioEndpoint();
    Regions awsRegion = Regions.fromName(s3Config.getAwsRegion());
    this.bucketName = s3Config.getCloudBucketName();

    // Start the counter with one because this class has a reference to it
    referenceCounter = new AtomicInteger(1);

    if (cloudAccessKey != null && cloudSecretKey != null) {
      if (minioEndpoint == null) {
        LOGGER.debug("config based credentials based s3 client");
        initializeS3ClientWithAccessKey(cloudAccessKey, cloudSecretKey, awsRegion);
      } else {
        LOGGER.debug("minio client");
        initializeMinioClient(cloudAccessKey, cloudSecretKey, awsRegion, minioEndpoint);
      }
    } else if (CommonUtils.isEnvSet(AWS_ROLE_ARN)
        && CommonUtils.isEnvSet(AWS_WEB_IDENTITY_TOKEN_FILE)) {
      LOGGER.debug("temporary token based s3 client");
      initializeWithWebIdentity(awsRegion);
    } else {
      LOGGER.debug("environment credentials based s3 client");
      // reads credentials from OS Environment
      initializeWithEnvironment(awsRegion);
    }
  }

  private void initializeWithEnvironment(Regions awsRegion) {
    this.s3Client = AmazonS3ClientBuilder.standard().withRegion(awsRegion).build();
  }

  private void initializeMinioClient(
      String cloudAccessKey, String cloudSecretKey, Regions awsRegion, String minioEndpoint) {
    awsCredentials = new BasicAWSCredentials(cloudAccessKey, cloudSecretKey);
    var clientConfiguration = new ClientConfiguration();
    clientConfiguration.setSignerOverride("VertaSignOverrideS3Signer");
    SignerFactory.registerSigner("VertaSignOverrideS3Signer", SignOverrideS3Signer.class);

    this.s3Client =
        AmazonS3ClientBuilder.standard()
            .withEndpointConfiguration(
                new AwsClientBuilder.EndpointConfiguration(minioEndpoint, awsRegion.getName()))
            .withPathStyleAccessEnabled(true)
            .withClientConfiguration(clientConfiguration)
            .withCredentials(new AWSStaticCredentialsProvider(awsCredentials))
            .build();
  }

  private void initializeS3ClientWithAccessKey(
      String cloudAccessKey, String cloudSecretKey, Regions awsRegion) {
    awsCredentials = new BasicAWSCredentials(cloudAccessKey, cloudSecretKey);
    this.s3Client =
        AmazonS3ClientBuilder.standard()
            .withRegion(awsRegion)
            .withCredentials(new AWSStaticCredentialsProvider(awsCredentials))
            .build();
  }

  public RefCountedS3Client getRefCountedClient() {
    return new RefCountedS3Client(awsCredentials, s3Client, referenceCounter);
  }

  private void initializeWithWebIdentity(Regions awsRegion) {
    // While creating RoleCredentials we have a set time (900 seconds (15 minutes))
    // in the AssumeRoleWithWebIdentityRequest so here expiration will be 900 seconds
    // so set cron to 1/3 of the duration of the credentials which will be 5 minutes.
    var durationSeconds = 900; /*900 seconds (15 minutes)*/
    var refreshTokenFrequency = durationSeconds / 3;
    LOGGER.trace(String.format("S3 Client refresh frequency %d seconds", refreshTokenFrequency));

    CommonUtils.scheduleTask(
        new RefreshS3ClientCron(bucketName, awsRegion, durationSeconds, this),
        0L /*initialDelay*/,
        refreshTokenFrequency /*periodic refresh frequency*/,
        TimeUnit.SECONDS);
  }

  void refreshS3Client(AWSCredentials awsCredentials, AmazonS3 s3Client) {
    // Once we get to this point, we know that we have a good new s3 client, so it's time to swap
    // it. No fail can happen now
    LOGGER.debug("Replacing S3 Client");
    try (RefCountedS3Client client = getRefCountedClient()) {
      // Decrement the current reference counter represented by this object pointing to it
      this.referenceCounter.decrementAndGet();

      // Swap the references
      this.referenceCounter = new AtomicInteger(1);
      this.awsCredentials = awsCredentials;
      this.s3Client = s3Client;
      LOGGER.debug("S3 Client replaced");
      // At the end of the try, the reference counter will be decremented again and shutdown will
      // be called
    }
  }
}
