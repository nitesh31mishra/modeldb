import loader from 'components/images/loader.gif';
import * as React from 'react';
import styles from './GlobalPreloader.module.css';

const GlobalPreloader = React.memo(() => {
  return (
    <div className={styles.global_preloader}>
      <img src={loader} />
    </div>
  );
});

export default GlobalPreloader;
