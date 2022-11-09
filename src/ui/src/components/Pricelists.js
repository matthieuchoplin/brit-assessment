import {useEffect, useState} from "react";
import {useApi} from "../contexts/ApiProvider";
import {Spinner} from "react-bootstrap";
import Pricelist from "./Pricelist";

export default function Pricelists() {
  const [showModal] = useState(false);
  const [pricelists, setPricelists] = useState();
  const api = useApi();
  useEffect(() => {
    (async () => {
      const response = await api.get('/pricelists');
      if (response.ok) {
        setPricelists(response.body.data);
      }
      else {
        setPricelists(null);
      }
    })();
  }, [api, showModal]);

  return (
    <>
      {pricelists === undefined ?
        <Spinner animation="border" />
      :
        <>
          {pricelists === null ?
             <p>You haven't created any pricelist yet.</p>
          :
            <>
              {pricelists.length === 0 ?
                <p>There are no pricelists.</p>
              :
                pricelists.map(pricelist => <Pricelist key={pricelist.id}
                                              pricelist={pricelist}
                                              pricelists={pricelists}
                                              setPricelists={setPricelists}
                />)
              }
            </>
          }
        </>
      }
    </>

  );
}
