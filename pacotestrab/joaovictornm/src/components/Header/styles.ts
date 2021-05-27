import styled from 'styled-components';

export const Container = styled.header`
  width: 100%;
  background: var(--green-webmural-900);
`;

export const Content = styled.div`
  max-width: 1328px;
  margin: 0 auto;
  padding: 0 2rem;

  font-size: 16px;
  font-weight: bold;

  text-align: center;

  display: flex;
  align-items: center;

  justify-content: space-between;   /* Option Right */

  color: var(--white);

  span {
    color: var(--orange-webmural-500);
  }

  @media (min-width: 768px) {
    padding: 0rem 4rem;
  }
`;

export const Logo = styled.div`
  cursor: pointer;
`;

export const ContentOptions = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

export const Option = styled.div`
  margin-left: 1rem;

  height: 4rem;
  
  display: flex;
  align-items: center;

  color: var(--white);

  cursor: pointer;

  transition: color 0.2s;

  &:hover {
    color: var(--orange-webmural-500);
  }

  svg:first-child {
    margin-right: 0.5rem;
  }
`;