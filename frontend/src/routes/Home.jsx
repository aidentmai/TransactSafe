import Hero from "../components/Hero";
import Navbar from "../components/navbar";

const Home = () => {
  return (
    <div className="flex flex-col">
      <Navbar />
      <div className="mt-96">
        <Hero />
      </div>
    </div>
  );
};

export default Home;
