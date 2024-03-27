import Navbar from "@/components/Partials/Layout/Navbar";
import styles from "./page.module.css";
import HeroSection from "@/components/Home/Hero";
import SubHero from "@/components/Home/SubHero";
import ServicesSection from "@/components/Home/Services";
import Tagline from "@/components/Home/Tagline";
import SuccessStories from "@/components/Home/Testimonials";
import Footer from "@/components/Home/Footer";

export default function Home() {
  return (
    <>
      <Navbar />
      <HeroSection />
      <SubHero />
      <ServicesSection />
      <Tagline />
      <SuccessStories />
      <Footer />
    </>
  );
}
