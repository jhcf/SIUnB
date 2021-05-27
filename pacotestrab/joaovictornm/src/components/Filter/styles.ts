import styled from 'styled-components';

export const Container = styled.header`
  width: 100%;
  max-width: 800px;
  background-color: var(--green-webmural-500);

  margin: 20px auto 0;
  border-radius: 10px;
  padding: 10px 4px;

  display: flex;
  flex-direction: column;
`;

export const Card = styled.div`
  width: 100%;

  display: flex;

  justify-content: space-between;
`;

export const Date = styled.div`
  font-size: 14px;
  width: 100%;
  text-align: center;
  background-color: var(--orange-webmural-300);
  border-radius: 6px;
  padding: 8px;
  font-weight: bold;
  margin: 0 8px;

  cursor: pointer;

  transition: transform 0.2s;

  &:hover {
    transform: scale(1.08);
  }
`

export const SearchText = styled.div`
  font-size: 16px;
  font-weight: bold;
`

export const Location = styled.input`
  font-size: 16px;
  font-weight: bold;
  border: none;
  padding: 4px;

  ::placeholder{
    font-size: 12px;
  }
`

export const Radius = styled.input`
  font-size: 16px;
  font-weight: bold;
  border: none;
  padding: 4px;

  ::placeholder{
    font-size: 12px;
  }
`