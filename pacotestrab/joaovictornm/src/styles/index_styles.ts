import styled from 'styled-components';

export const Container = styled.div`
  width: 100%;
  min-height: calc(100vh - 64px);
  background: var(--orange-webmural-100);
`;

export const Content= styled.div`
  max-width: 1328px;
  margin: 0 auto;
  padding: 2rem 2rem;

  @media (min-width: 768px) {
    padding: 2rem 44px;
  }
`;