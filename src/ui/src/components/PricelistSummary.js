import { Modal} from "react-bootstrap";
import Button from "react-bootstrap/Button";

export default function PricelistSummary(props) {
  const {pricelist} = props;
  const goBack = () => {
    props.toggleModal(null);
}
  return <div>
    <Modal show={props.isOpen} animation={false} size="xl">
      <Modal.Body>
          <p>Total Cost: {pricelist.summary}</p>
          <Button variant="secondary" onClick={goBack}
            >Back</Button>
      </Modal.Body>
    </Modal>
  </div>
};
