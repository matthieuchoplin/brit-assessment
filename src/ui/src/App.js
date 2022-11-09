import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import ApiProvider from './contexts/ApiProvider';
import FlashProvider from "./contexts/FlashProvider";
import PricelistPages from "./pages/PricelistPages";
import PricelistPage from "./pages/PricelistPage";
import ItemPage from "./pages/ItemPage";

export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <FlashProvider>
          <ApiProvider>
            <Routes>
              <Route path="*" element={
                  <Routes>
                    <Route path="/" element={<Navigate to="/pricelist/1" />} />
                    <Route path="/pricelists" element={<PricelistPages />} />
                    <Route path="/pricelist/:id" element={<PricelistPage />} />
                    <Route path="*" element={<Navigate to="/pricelist/1" />} />
                    <Route path="/item/:id" element={<ItemPage />} />
                  </Routes>
              } />
            </Routes>
          </ApiProvider>
        </FlashProvider>
      </BrowserRouter>
    </Container>
  );
}
