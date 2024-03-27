import styles from "./subhero.module.css";
export default function SubHero() {
  return (
    <section className={styles.container}>
      <p className="green_title">Top rated platform in the world</p>
      <h1 className={styles.title}>
        Empower your journey to success with the guidiance of our seasoned
        mentors and coaches, and meet our handpicked experts and coaches, who
        are dedicated
      </h1>
      <div className={styles.bottom}>
        <div className={styles.avatar_stack}>
          <img src="/subHero/1.jpeg" alt="" className={styles.avatar} />
          <img src="/subHero/2.jpeg" alt="" className={styles.avatar} />
          <img src="/subHero/3.jpeg" alt="" className={styles.avatar} />
          <span className={styles.overflow_indicator}>+10</span>
        </div>
        <div>
          <h3>Best Mentors 2023</h3>
          <p>Top Rated</p>
        </div>
      </div>
    </section>
  );
}
