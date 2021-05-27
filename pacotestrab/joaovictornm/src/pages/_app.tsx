import { AppProps } from 'next/app'

import GlobalStyle from '../styles/global'

import { Header } from '../components/Header'
import { Filter } from '../components/Filter'
import { Container } from '../styles/index_styles'


function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Container>
      <Header />
      <Filter />
      <Component {...pageProps} />
      <GlobalStyle/>
    </Container>
 )
}

export default MyApp
