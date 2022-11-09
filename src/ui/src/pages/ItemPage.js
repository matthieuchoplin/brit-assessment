import Body from '../components/Body';
import {useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {useApi} from "../contexts/ApiProvider";
import Button from "react-bootstrap/Button";
import {Form} from "react-bootstrap";
import {useFlash} from "../contexts/FlashProvider";
import Spinner from "react-bootstrap/Spinner";

export default function ItemPage() {
  const { id } = useParams();
  const [item, setItem] = useState();
  const api = useApi();
  const flash = useFlash();
  const navigate = useNavigate();

  useEffect(() => {
    (async () => {
      const response = await api.get('/items/' + id);
      setItem(response.ok ? response.body : null);
    })();
  }, [id, api]);

  const handleChange = (e ) => {
    e.preventDefault();
    e.persist();
    setItem(item => {
      return {...item,
      [e.target.name]: e.target.value}
    })
  }

  const saveData = async () => {
    const data = await api.put(`/items/${id}`, {
        name: item.name,
        price: item.price
      });
    if (data.ok) {
        flash(`Item ${item.name} updated with price ${item.price}!`, 'success');
        navigate(`/pricelist/${item.pricelist_id}`);
      }

  }
  return (

    <Body sidebar>
      {item === undefined ?
        <Spinner animation="border" />
      :
        <>
            <Form>
              <Form.Group className="mb-3" controlId="alertForm.inputName">
                <Form.Label>Edit item</Form.Label>
                <Form.Control
                  data-testid="inputName"
                  type="name"
                  name="text"
                  autoFocus
                  value={item.name}
                  defaultValue={item.name}
                  onChange={handleChange}
                />
                <Form.Control
                  data-testid="inputPrice"
                  type="number"
                  name="price"
                  autoFocus
                  value={item.price}
                  defaultValue={item.price}
                  onChange={handleChange}
                />
              </Form.Group>
              <Form.Group
                className="mb-3">
                <Button className='mr-2 btn-alert' variant="primary"
                        onClick={saveData}>Save</Button>
              </Form.Group>
            </Form>
            </>
        }
    </Body>
  );
}
