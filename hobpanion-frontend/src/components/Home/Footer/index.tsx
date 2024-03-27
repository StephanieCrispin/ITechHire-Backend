import styles from "./footer.module.css";
import { RiFacebookFill } from "react-icons/ri";
import { FaInstagram } from "react-icons/fa";
import { FaTwitter } from "react-icons/fa";
import { BiBasketball } from "react-icons/bi";
import Image from "next/image";
const FOOTER = [
  {
    title: "Product",
    items: [
      "Security and Privacy",
      "Integrations",
      "Pricing",
      "Help Docs",
      "Pricing",
    ],
  },
  {
    title: "Benefits",
    items: [
      "Checking Account",
      "Find Mentor",
      "Pricing",
      "Help Docs",
      "Pricing",
    ],
  },
  {
    title: "Company",
    items: [
      "Checking Account",
      "Find Mentor",
      "Pricing",
      "Help Docs",
      "Pricing",
    ],
  },
  {
    title: "Privacy Policy",
    items: [
      "Checking Account",
      "Find Mentor",
      "Pricing",
      "Help Docs",
      "Pricing",
    ],
  },
];

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className={styles.container}>
      <div className={styles.top_section}>
        <div className={styles.footer_logo_item}>
          <Image
            src="/nav/logo.png"
            className={styles.logo}
            width={160}
            height={0}
            alt="Hobpanion"
          />

          <div className={styles.subtitle}>
            Empowering your Potential, Guiding your success
          </div>
        </div>
        {FOOTER.map(({ title, items }, index) => {
          return (
            <div className={styles.footer_item} key={index}>
              <h3 className={styles.title}>{title}</h3>
              {items.map((item, index) => (
                <p key={index}>{item}</p>
              ))}
            </div>
          );
        })}
      </div>

      <div className={styles.bottom_section}>
        <span className={styles.bottom_text}>
          <p>&copy; {currentYear} HobPanioN. All rights reserved.</p>
        </span>
        <div className={styles.icons}>
          <RiFacebookFill size={25} />
          <FaInstagram size={25} />
          <FaTwitter size={25} />
          <BiBasketball size={25} />
        </div>
      </div>
    </footer>
  );
}
