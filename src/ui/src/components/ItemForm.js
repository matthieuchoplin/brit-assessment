import {Form, Modal} from "react-bootstrap";
import Button from "react-bootstrap/Button";
import {useState} from "react";
import {useApi} from "../contexts/ApiProvider";
import {useFlash} from "../contexts/FlashProvider";
import {useNavigate} from "react-router-dom";


const emptyItem = {
  name: "",
  price: ""
}

export default function ItemForm(props) {
  const [fields, setFields] = useState(emptyItem);
  const navigate = useNavigate();
  const api = useApi();
  const flash = useFlash();

  const clearFormData = () => {
    props.toggleModal(null);
    setFields(emptyItem);
  }

  const handleChange = (e ) => {
    e.preventDefault();
    e.persist();
    setFields(existingFields => {
      return {...existingFields,
      [e.target.name]: e.target.value}
    })
  }

  const saveData = async () => {
    const pricelist_id = props.pricelist_id
    const data = await api.post('/items', {
        name: fields.text,
        pricelist_id: pricelist_id,
        price: fields.price
      });
    if (data.ok) {
        flash(`Item ${fields.text} created!`, 'success');
        navigate(`/pricelist/${pricelist_id}`);
        props.toggleModal(null);
      }
  }
      return <div>
    <Modal show={props.isOpen} animation={false} size="xl">
      <Modal.Body>
        <Form>
          <Form.Group className="mb-3" controlId="itemForm.InputTitle">
            <Form.Label>Item</Form.Label>
            <Form.Control
              data-testid="inputTitle"
              type="text"
              name="text"
              autoFocus
              value={fields.title}
              onChange={handleChange}
            />
          </Form.Group>
                    <Form.Group className="mb-3" controlId="itemForm.InputPrice">
            <Form.Label>Price</Form.Label>
            <Form.Control
              data-testid="inputPrice"
              type="number"
              name="price"
              autoFocus
              value={fields.price}
              onChange={handleChange}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Button
                id="add-item-button-form"
                className='mr-2 btn-item'
                variant="primary"
                onClick={saveData}
            >Save</Button>
            <Button variant="secondary"
                    onClick={clearFormData}
            >Cancel</Button>
          </Form.Group>
        </Form>
      </Modal.Body>
    </Modal>
  </div>
};
