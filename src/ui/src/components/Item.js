import { Link } from 'react-router-dom';
import {PencilFill} from "react-bootstrap-icons";

export default function Item(props ) {
    const {item} = props;
  return (
      <tr>
        <td>{item.name}</td>
        <td>{item.price}</td>
        <td><Link to={'/item/' + item.id}><PencilFill /></Link></td>
      </tr>
  );
}
