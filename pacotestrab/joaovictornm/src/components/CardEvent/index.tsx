import { Card, Title, Description, Text, Date, Image, Location } from './styles'
import Link from 'next/link'

export function CardEvent(props) {
  console.log(props.osm[0])
  return (
    <Card>
      { props.osm[0]?.startsWith('https://') ? (
        <Link href={props.osm[0]}>
          <Image
            src="images/map.png"
            alt=""
          />
        </Link>
      ) : (
        <Image
          src="images/map.png"
          alt=""
        />
      )}
      <Title>
        {props.name}
      </Title>
      <Description>
        <Text>{props.description}</Text>
        <Location>Localização: {props.osm}</Location>
      </Description>
      <Date>Dias do evento:
        <span> {props.days?.map((day) => (day + ', ')) || ' Sem data'}</span>
      </Date>
    </Card>
  )
}