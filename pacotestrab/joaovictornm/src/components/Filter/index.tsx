import { Card, Date, Container, SearchText, Location, Radius } from './styles'
import Link from 'next/link'

export function Filter() {
  return (
    <Container>
      <Card>
        <Date>19/05/2021</Date>
        <Date>20/05/2021</Date>
        <Date>21/05/2021</Date>
        <Date>22/05/2021</Date>
        <Date>23/05/2021</Date>
        <Date>24/05/2021</Date>
      </Card>
      <SearchText>
        Pesquise por cidade, bairro ou código postal
      </SearchText>
      <Location placeholder="Localização">

      </Location>
      <Radius placeholder="Raio">

      </Radius>
    </Container>
  )
}