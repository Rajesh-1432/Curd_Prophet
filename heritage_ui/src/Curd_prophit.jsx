import React, { useState } from "react";
import logo from "./assets/logo.png";
import profile from "./assets/profile.png";
import { Form, Input, Button, Row, Col, Table,Spin } from "antd";
import { LoadingOutlined, CloseOutlined } from "@ant-design/icons";

const Curd_prophit = () => {
  const [apiResponse, setApiResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [formValues, setFormValues] = useState(null);

  const handleSubmit = async (values) => {
    try {
      setLoading(true);
      setFormValues(values);

      const response = await fetch(
        "http://127.0.0.1:5000/predict_sales_quantity",
        
        {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            from_date: values.From_Date,
            to_date: values.To_Date,
            material_code: values.Meterial_Code,
            sales_office_id: values.Sales_Office_Id,
          }),
        }
      );

      const data = await response.json();
      setApiResponse(data);

      console.log("API Response:", data);
    } catch (error) {
      setLoading(false);
      console.error("Error calling API:", error);
    } finally {
      setLoading(false);
    }
  };
  const columns =
    Array.isArray(apiResponse) &&
    apiResponse.map(({ date }) => ({
      title: date,
      dataIndex: date,
      key: date,
      render: (text) => <span>{text}</span>,
    }));

  const dataSource = [
    {
      key: "sales_quantity",
      ...(Array.isArray(apiResponse)
        ? apiResponse.reduce((acc, { date, sales_quantity }) => {
            acc[date] = sales_quantity;
            return acc;
          }, {})
        : {}),
    },
  ];

  return (
    <div>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          height: "40px",
          margin: "-8px",
          padding: "30px",
          backgroundColor: "yellow",
        }}
      >
        <img src={logo} alt="Logo" style={{height:'70px',width:'120px'}} />

        <h1 style={{ margin: "0 auto" }}>CURD PROPHET</h1>

        <div style={{ display:'flex ' }}>
          
          <p style={{fontSize:'15px'}}><img
            src={profile}
            alt="Dummy Profile"
            style={{ width: "20px", height: "20px", borderRadius: "50%" }}
          /><b>Profile <br /> mail:</b> heritage@gmail.com <br />
              <b>Name:</b> Rajesh Dumpala</p>
        </div>
      </div>
      <div>
        <div
          style={{
            width: "95%",
            height: "50px",
            margin: "0 auto",
            marginTop: "30px",
            paddingTop: "15px",
            border: "0.5px solid #fff",
            borderRadius: "8px",
            boxShadow: "0 4px 4px rgba(0, 0, 0, 0.1), 0 0 4px green",
            backgroundColor: "#fff",
            textAlign: "center",
          }}
        >
          <Form name="curdProphet" onFinish={handleSubmit} labelAlign="left">
            <Row justify="center" gutter={16}>
              <Col span={4}>
                <Form.Item
                  label="From Date"
                  name="From_Date"
                  rules={[
                    { required: true, message: "Please enter the From Date" },
                  ]}
                >
                  <Input type="date" />
                </Form.Item>
              </Col>
              <Col span={4}>
                <Form.Item
                  label="To Date"
                  name="To_Date"
                  rules={[
                    { required: true, message: "Please enter the To Date" },
                  ]}
                >
                  <Input type="date" placeholder="select To Date" />
                </Form.Item>
              </Col>
              <Col span={4}>
                <Form.Item
                  label="Material Code"
                  name="Meterial_Code"
                  rules={[
                    {
                      required: true,
                      message: "Please enter the Material Code",
                    },
                  ]}
                >
                  <Input type="text" placeholder="Material Code" />
                </Form.Item>
              </Col>
              <Col span={4}>
                <Form.Item
                  label="Sales Office ID"
                  name="Sales_Office_Id"
                  rules={[
                    {
                      required: true,
                      message: "Please enter the Sales Office ID",
                    },
                  ]}
                >
                  <Input type="text" placeholder="Sales Office ID" />
                </Form.Item>
              </Col>
              <Col span={3}>
                <Form.Item>
                  <Button
                    type="primary"
                    htmlType="submit"
                    style={{ width: "100%", backgroundColor: "green" }}
                  >
                    Submit
                  </Button>
                </Form.Item>
              </Col>
            </Row>
          </Form>
        </div>
        <div
        style={{
          width: "98%",
          height: "350px",
          margin: "0 auto",
          marginTop: "30px",
          border: "0.5px solid #fff",
          borderRadius: "8px",
          boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1), 0 0 6px #E03FD8",
          backgroundColor: "#fff",
          textAlign: "left",
          fontFamily: "roboto",
          overflowX: "auto", // Add horizontal scrollbar
        }}
      >
        {loading ? (
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              height: "100%",
             
            }}
          >
            <Spin indicator={<LoadingOutlined style={{ fontSize: 40 }} spin />} /> 
            <h3>Loading...</h3>
          </div>
        ) : (
          <div>
            {apiResponse && apiResponse.length > 0 && columns ? (
              <Table dataSource={dataSource} columns={columns} />
            ) : (
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  height: "100%",
                  fontSize: '24px',
                  color: 'gray',
                  paddingTop:'100px'
                }}
              >
                <CloseOutlined style={{ marginRight: '8px' }} />
                No data available
              </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Curd_prophit;
