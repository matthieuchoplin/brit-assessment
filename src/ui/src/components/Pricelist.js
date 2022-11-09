import Stack from 'react-bootstrap/Stack';
import { Link } from 'react-router-dom';

export default function Pricelist(props ) {
    const {pricelist} = props;
  return (
      <div>
        <Stack direction="horizontal" gap={3} className="Pricelist">
          <div>
            <Link to={`/pricelist/${pricelist.id}`}><p>Pricelist id: {pricelist.id}</p></Link>
          </div>
        </Stack>
     </div>
  );
}
