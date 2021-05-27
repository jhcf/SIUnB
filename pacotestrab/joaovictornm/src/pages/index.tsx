import Head from 'next/head';
import { Container, Content } from '../styles/index_styles';
import { CardList } from "../components/CardList";

export default function Home() {
  return (
    <>
      <Head>
        <title>
          WebMural | Se liga nessa parada
        </title>
      </Head>
      <Content>
        <CardList />
      </Content>
    </>
  )
}
