import styles from "./tagline.module.css";
export default function Tagline() {
  return (
    <section className={styles.container}>
      <div className={styles.header}>
        <h1 className="general_title">Guidiance with the best platform</h1>
        <p className={styles.sub_title}>
          Experience the power of guidiance with the best platform wit
          mentorship and coaching. Our commitment to your success is unwavering
          and we&apos;ve carafully curated a network of seasoned experts who are
          dedicated.
        </p>
        <button className="button">Learn More</button>
      </div>

      <img src="/tagline/spiral_image.png" alt="Tagline Image" />
    </section>
  );
}
