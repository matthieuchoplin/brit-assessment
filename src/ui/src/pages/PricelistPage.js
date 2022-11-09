import Body from '../components/Body';
import {useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {useApi} from "../contexts/ApiProvider";
import Spinner from "react-bootstrap/Spinner";
import Stack from "react-bootstrap/Stack";
import Button from "react-bootstrap/Button";
import ItemForm from "../components/ItemForm";
import Item from "../components/Item";

export default function PricelistPage() {
  const { id } = useParams();
  const [items, setItems] = useState();
  const [pricelist, setPricelist] = useState();
  const api = useApi();
  const [showModal, setShowModal] = useState(false);

  const toggleModal = () => {
    setShowModal(true);
  }

  useEffect(() => {
    (async () => {
      const resp = await api.get(`/pricelists/${id}/items`);
      setItems(resp.ok ? resp.body.data : null);
      const resp2 = await api.get(`/pricelists/${id}`);
      setPricelist(resp2.ok ? resp2.body : null);
    })();
  }, [id, api, showModal]);

  return (
    <Body sidebar>
      {pricelist === undefined ?
        <Spinner animation="border" />
      :
        <>
          {pricelist === null ?
            <p>Pricelist not found.</p>
          :
            <h1>{pricelist.title}</h1>
          }
        </>
      }
      {items === undefined ?
        <Spinner animation="border" />
      :
        <>
          {items === null ?
            <p>Item not found.</p>
          :
            <>
              <Stack direction="horizontal" gap={4}>
                <div>
                  <Button id="button-add-item" variant="primary" onClick={() => toggleModal(null)}>Add Item</Button>{' '}
                  <>
                    {items === null ?
                       <p>Could not retrieve items.</p>
                    :
                      <>
                        {items.length === 0 ?
                          <p>There are no items.</p>
                        :
                            <table>
                              <tr>
                                <th>Item</th>
                                <th>Price</th>
                              </tr>
                              {items.map(q => <Item key={q.id} item={q} items={items} setItems={() => setItems}/>)}
                            </table>

                        }
                      </>
                    }
                  </>
                </div>
              </Stack>
            </>
          }
          <ItemForm
              isOpen={showModal}
              toggleModal={setShowModal}
              pricelist_id={id}
          />
        </>
      }
    </Body>
  );
}
