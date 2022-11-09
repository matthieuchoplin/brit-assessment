import { createContext, useContext } from 'react';
import PricelistApiClient from '../PricelistApiClient';

const ApiContext = createContext();

export default function ApiProvider({ children }) {
  const api = new PricelistApiClient();

  return (
    <ApiContext.Provider value={api}>
      {children}
    </ApiContext.Provider>
  );
}

export function useApi() {
  return useContext(ApiContext);
}
