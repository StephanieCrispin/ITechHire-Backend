import styles from "./hero.module.css";
export default function HeroSection() {
  return (
    <section className={styles.container}>
      <div className={styles.intro}>
        <p className={styles.intro_highlight}>New in v5.3</p>
        <p className="green_title">TOP RATED PLATFORM</p>
      </div>
      <h1 className={styles.title}>
        Unlock Your Potential with a{" "}
        <span className={styles.green_header}>Best Mentor</span>
      </h1>
      <div className={styles.subtitle}>
        Our mentorship program is designed to connect you with experienced and
        passionate mentors
      </div>
      <div className={styles.search}>
        <input placeholder="Find your favourite mentors" type="search" />
        <button className="button">Search Now</button>
      </div>
      <h2 className={styles.partners_title}>OUR PARTNERS</h2>

      <div className={styles.partners}>
        <div className={styles.partner_logos}>
          <div>
            <img
              src="/hero/google.png"
              alt=""
              className={styles.partner_logo}
            />
          </div>

          <div>
            <img src="/hero/etsy.png" alt="" className={styles.partner_logo} />
          </div>

          <div>
            <img src="/hero/xbox.png" alt="" className={styles.partner_logo} />
          </div>
          <div>
            <img
              src="/hero/microsoft.png"
              alt=""
              className={styles.partner_logo}
            />
          </div>
        </div>
      </div>
    </section>
  );
}
