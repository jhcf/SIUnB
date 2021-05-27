import { createGlobalStyle } from 'styled-components';

export default createGlobalStyle`
* {
  margin: 0;
  padding: 0;
  outline: 0;
  box-sizing: border-box
}

*.focus {
  outline: none
}

html, body, #root {
  height: 100%;
}

body {
  -webkit-font-smoothing: antialiased;
}

body, input, button {
  font: 14px 'Roboto', sans-serif;
}

a {
  text-decoration: none;
}

ul {
  list-style: none;
}

button { 
  cursor: pointer 
}

:root {
  --white: #FFF;

  --gray-50: #F7FAFC;
  --gray-100: #EDF2F7;
  --gray-300: #CBD5E0;
  --gray-500: #718096;
  --gray-900: #171923;

  --green-webmural-50: #E6FFFA;
  --green-webmural-100: #B2F5EA;
  --green-webmural-300: #4FD1C5;
  --green-webmural-500: #319795;
  --green-webmural-900: #1D4044;

  --orange-webmural-50: #FFFAF0;
  --orange-webmural-100: #FEEBC8;
  --orange-webmural-300: #F6AD55;
  --orange-webmural-500: #DD6B20;
  --orange-webmural-900: #652B19;
}
`;