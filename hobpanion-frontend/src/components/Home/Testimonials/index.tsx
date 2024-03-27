import styles from "./testimonials.module.css";
import { AiFillStar } from "react-icons/ai";
const TESTIMONIAL_CARDS = [
  {
    name: "Esteban Vergas",
    occupation: "Bussiness Man",
    title: "They not only provide deep insights into the industry",
    subtitle:
      "I am very fortunate to be part of the mentorship program. My mentor has provided invaluable guidiance in growing my bussiness",
    img: "/subHero/1.jpeg",
  },
  {
    name: "Esther Tee",
    occupation: "Bussiness Man",
    title: "They not only provide deep insights into the industry",
    subtitle:
      "I am very fortunate to be part of the mentorship program. My mentor has provided invaluable guidiance in growing my bussiness",
    img: "/subHero/2.jpeg",
  },
  {
    name: "Rapheal Gologolo",
    occupation: "UI Enthusiast",
    title: "They not only provide deep insights into the industry",
    subtitle:
      "I am very fortunate to be part of the mentorship program. My mentor has provided invaluable guidiance in growing my bussiness",
    img: "/subHero/3.jpeg",
  },
];

export default function SuccessStories() {
  return (
    <section className={styles.container}>
      <div className={styles.header}>
        <p className="green_title">Stories and testimonials</p>
        <h1 className="general_title">Success Stories Our Client</h1>
        <p className="general_subtitle">
          is simple dummy text of the printing and typesetting industry, Lorem
          Ipsum has been the industry&apos;s standard
        </p>
      </div>

      <div className={styles.cards}>
        {TESTIMONIAL_CARDS.map(
          ({ name, occupation, title, subtitle, img }, index) => {
            return (
              <div key={index} className={styles.card}>
                <div className={styles.card_header}>
                  <img src={img} alt={name} className={styles.image} />
                  <div className={styles.content}>
                    <p>{name}</p>
                    <p>{occupation}</p>
                  </div>
                </div>
                <p className={styles.card_title}>{title}</p>
                <p className={styles.card_subtitle}>{subtitle}</p>
                <div className={styles.stars}>
                  {Array(5).fill(
                    <AiFillStar className="star" color="#ffc107" size={25} />
                  )}
                </div>
              </div>
            );
          }
        )}
      </div>
    </section>
  );
}
