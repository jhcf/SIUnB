import { Container, Content, ContentOptions, Option, Logo } from './styles'
import { FaUser } from "react-icons/fa";

export function Header() {
  return (
    <Container>
      <Content>
        <Logo>
          <h2>Web<span>Mural</span>;</h2>
        </Logo>
        <ContentOptions>
          <Option>
            <FaUser />
            Minha Conta
          </Option>
        </ContentOptions>
      </Content>
    </Container>
  )
}