import type { NextPage } from 'next';
import Head from 'next/head';
import Image from 'next/image';
import styles from '../styles/Home.module.css';

const Home: NextPage = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold underline text-red-500">
        Hello world!
      </h1>
    </div>
  );
};

export default Home;
