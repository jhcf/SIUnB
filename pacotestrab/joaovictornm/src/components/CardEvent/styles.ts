import styled from 'styled-components';

export const Card = styled.div`
  background-color: var(--green-webmural-500);
  width: 100%;
  max-width: 800px;

  margin: 20px;
  border-radius: 10px;

  display: flex;
  flex-direction: column;

  transition: transform 0.2s;

  &:hover {
    transform: translateY(-10px);
  }

  @media (max-width: 767px) {
    margin-top: 20px;
  }
`;

export const Image = styled.img`
  padding: 12px;
  width: 100%;
  height: 200px;
  object-fit: cover;
  cursor: pointer;
`;

export const Title = styled.div`
  text-align: center;
  width: 100%;
  padding: 12px;
  font-size: 16px;
  font-weight: bold;
`;

export const Description = styled.div`
  width: 100%;
  padding: 12px;
`;

export const Text = styled.div`
  font-size: 16px;
  color: var(-orange-webmural-500);
`

export const Date = styled.div`
  font-size: 14px;
  color: var(-orange-webmural-500);
  text-align: end;
  padding: 12px;
  font-weight: bold;
  
  span {
    font-weight: normal;
  }
`

export const Location = styled.div`
  margin-top: 10px;
  font-size: 16px;
  text-align: justify;
`