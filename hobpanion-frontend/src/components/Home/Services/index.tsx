import styles from "./services.module.css";

export default function ServicesSection() {
  return (
    <section className={styles.container}>
      <div className={styles.header_section}>
        <p className="green_title">Discover our Services</p>
        <h1 className="general_title">Welcome to HobPanioN</h1>
        <p className="general_subtitle">
          Connect with mentors and coaches who are committed to seeing you
          thrive in your personal and proffesional life
        </p>
      </div>
      <div className={styles.cards}>
        <div className={styles.card_1}>
          <p className={styles.card_title}>Best Experience</p>
          <h1 className={styles.title}>
            Access a diverse range of mentors and coaches
          </h1>
          <p className="general_subtitle">
            Connect with mentors and coaches who are committed to seeing you
            thrive in your personal and proffesional life
          </p>
          <button className={styles.card_button}>Apply Now for Free</button>
        </div>
        <div className={styles.card_2}>
          <p className={styles.card_title}>Rise and grow together</p>
          <h1 className={styles.title}>Connect with over 1M+ best mentors</h1>
          <p className={styles.subTitle}>
            Recieve one on one guidiance customized to your specific needs and
            seize opportunities.
          </p>
          <div className={styles.avatar_section}>
            <div className={styles.avatar_stack}>
              <img src="/subHero/1.jpeg" alt="" className={styles.avatar} />
              <img src="/subHero/2.jpeg" alt="" className={styles.avatar} />
              <img src="/subHero/3.jpeg" alt="" className={styles.avatar} />
              <span className={styles.overflow_indicator}>+10</span>
            </div>
            <p className={styles.avatar_title}>Best Mentor</p>
          </div>
        </div>
      </div>
    </section>
  );
}
