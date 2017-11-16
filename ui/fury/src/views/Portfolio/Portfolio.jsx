import React, { Component } from 'react';
import { Grid, Row, Col, Table } from 'react-bootstrap';
import Button from 'elements/CustomButton/CustomButton.jsx';
import Card from 'components/Card/Card';
import {iconsArray} from 'variables/Variables.jsx';
import { FormGroup, ControlLabel, FormControl, Modal } from 'react-bootstrap';
import { GridLoader } from 'react-spinners';



var api =  require('../../utils/api');

const MyRow = function(props){
  const {checked, row, onChange, onChecked} = props;
  return (
    <div>
      <Row>
      <div key="1" className="col-md-1">
          <FormGroup>
                <input
                    className="pf-checkbox" 
                    type="checkbox" 
                    checked={checked}
                    onChange={onChecked}
                />
          </FormGroup>
      </div>
      <div key="2" className="col-md-2">
          <FormGroup>
                <ControlLabel>Stock</ControlLabel>
                <FormControl 
                     className="pf-stock" 
                     type="text"
                     bsClass= "form-control"
                     autoFocus= "true"
                     placeholder="Stock"
                     onChange= {onChange}
                     value={row.stock}
                />
          </FormGroup>
      </div>
      <div key="3" className="col-md-3">
          <FormGroup>
                <ControlLabel>Shares</ControlLabel>
                <FormControl
                     className="pf-shares"   
                     type= "number"
                     bsClass= "form-control"
                     placeholder="Number of Shares"
                     onChange= {onChange}
                     value={row.shares}
                />
          </FormGroup>
      </div>
      <div key="4" className="col-md-3">
          <FormGroup>
                <ControlLabel>Price</ControlLabel>
                <FormControl 
                     className="pf-price"  
                     type= "number"
                     bsClass= "form-control"
                     placeholder="Price"
                     onChange= {onChange}
                     value={row.price}
                />
          </FormGroup>
      </div>
      <div key="5" className="col-md-3">
          <FormGroup>
                <ControlLabel>Notes</ControlLabel>
                <FormControl
                     className="pf-notes"   
                     type= "text"
                     bsClass= "form-control"
                     placeholder="Notes"
                     onChange= {onChange}
                     value={row.notes}
                />
          </FormGroup>
      </div>
    </Row>
    </div>
  );
}


class Portfolio extends Component {

    constructor(props) {
        super(props);
        this.state = {
          rows: [],
          loading: true,
          portfolio: []
        };
    }

    updateValue(e, idx){
        var className = e.target.className;
        const rows = this.state.rows;
        if(className.indexOf("stock") > -1) {
            rows[idx].stock = e.target.value;
        } else if (className.indexOf("shares") > -1) {
            rows[idx].shares = e.target.value;
        } else if (className.indexOf("price") > -1) {
            rows[idx].price = e.target.value;
        } else if (className.indexOf("notes") > -1) {
            rows[idx].notes = e.target.value;
        }
        this.setState({
            rows,
        });
    }
      
    onChecked(idx){
        const rows = this.state.rows;
        rows[idx].checked = !rows[idx].checked;
        this.setState({
            rows,
        });
    } 
      
    addRow(){
        const rows = [...this.state.rows, 
                      {stock:'', shares: 1, price: '', notes: '', checked: false}
                     ];
        this.setState({
            rows,
        });
    }

    deleteRows(){
        const rows = this.state.rows.filter((e, i) => !e.checked);
        this.state.rows = rows;
        this.setState({
          rows,
        });
        
    }

    addToFolio(){
        api.addToFolio(this.state.rows)
          .then(function (response) {
          });
    }

    componentDidMount() {
        var self = this;
        api.getPortfolio()
          .then(function (response) {
            var portfolio = [];
            if(response.success) {
                var data = response.data;
                var item;
                for(item in data) {
                    var fields = data[item].fields;
                    var row = 
                    {
                        stock:fields.stock, 
                        shares: fields.shares, 
                        price: fields.price, 
                        notes: fields.notes
                    };
                    portfolio.push(row);
                }
            } else {
                
            }
            self.setState({
               loading: false,
               portfolio: portfolio
            });
          });
    }

    render() {
        let close = () => this.setState({ show: false });
        return (
            <div className="content">
                <Grid fluid>
                    <Row>
                        <Col md={12}>
                            <Card
                                title="Portfolio"
                                ctAllIcons
                                category={
                                    <span>
                                        Manage your holdings here
                                    </span>
                                }
                                content={
                                    <div>
                                        <Modal
                                          bsSize="small"
                                          show={this.state.loading}
                                          onHide={close}
                                          container={this}
                                          //aria-labelledby="contained-modal-title"
                                        >
                                          <Modal.Body>
                                            <GridLoader
                                              color={'#123abc'}
                                              loading={this.state.loading}
                                            />
                                          </Modal.Body>
                                        </Modal>
                                        <Table striped hover>
                                        <thead>
                                        <tr>
                                        {   
                                                this.state.portfolio.length > 0 && Object.keys(this.state.portfolio[0]).map((prop,key) => {
                                                    return (
                                                        <th key={key}>{prop}</th>
                                                    );
                                                })
                                        }
                                        </tr>
                                        </thead>
                                        <tbody>
                                            {
                                                this.state.portfolio.map((row,key) => {
                                                    return (
                                                        <tr key={key}>{
                                                            Object.keys(row).map((prop,key)=> {
                                                                return (
                                                                    <td  key={key}>{row[prop]}</td>
                                                                );
                                                            })
                                                        }</tr>
                                                    )
                                                })
                                            }
                                        </tbody>
                                        </Table>
                                        <form>
                                            <Button
                                                bsSize="sm"
                                                bsStyle="info"
                                                fill
                                                onClick={()=>this.addRow()}
                                            >
                                            Add
                                            </Button>
                                            {this.state.rows.length > 0 && 
                                                <Button
                                                    bsSize="sm"
                                                    bsStyle="info"
                                                    fill
                                                    onClick={()=>this.deleteRows()}
                                                >
                                                Remove
                                                </Button>
                                            }
                                            {this.state.rows.map((row, idx) => {
                                              return(
                                                  <MyRow 
                                                    key={idx} 
                                                    row={row}
                                                    checked={row.checked}
                                                    onChange={(e) => this.updateValue(e,idx)} 
                                                    onChecked={() => this.onChecked(idx)}
                                                  /> 
                                                )
                                            })
                                            }
                                            {this.state.rows.length > 0 && 
                                                <Button
                                                    bsSize="sm"
                                                    bsStyle="info"
                                                    fill
                                                    onClick={()=>this.addToFolio()}
                                                >
                                                Submit
                                                </Button>
                                            }   
                                        </form>
                                    </div>
                                }
                            />
                        </Col>
                    </Row>
                </Grid>
            </div>
        );
    }
}

export default Portfolio;
