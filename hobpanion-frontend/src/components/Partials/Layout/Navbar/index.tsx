import Image from "next/image";
import styles from "./navbar.module.css";
import Link from "next/link";
export default function Navbar() {
  return (
    <nav className={styles.container}>
      <div className={styles.left_nav}>
        <Image
          src="/nav/logo.png"
          className={styles.logo}
          width={160}
          height={0}
          alt="Hobpanion"
        />

        <div className={styles.nav_items}>
          <Link href="#">About Us</Link>
          <Link href="#">Pricing</Link>
          <Link href="#">FAQs</Link>
        </div>
      </div>
      <div className={styles.right_nav}>
        <Link href="#" className={styles.apply_cta}>
          Apply Now For Free
        </Link>

        <Link href="#" className={styles.sign_in}>
          Sign In
        </Link>
      </div>
    </nav>
  );
}
