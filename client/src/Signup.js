import React, { useEffect, useState } from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

const initialValues = {
  username: "",
  name: "",
  password: "",
};

const validationSchema = Yup.object({
  username: Yup.string()
    .min(3, "username must be at least 3 characters")
    .required("Username is required"),
  name: Yup.string()
    .min(3, "username must be at least 3 characters")
    .required("Name is required"),
  password: Yup.string()
    .min(3, "username must be at least 3 characters")
    .required("Name is required"),

  // email: Yup.string()
  //   .email("Invalid email address")
  //   .required("Email is required"),
  // message: Yup.string().required("Message is required"),
});

const Signup = () => {
  // const [users, setUsers] = useState([]);

  // useEffect(() => {
  //   fetch("/users")
  //     .then((response) => response.json())
  //     .then((data) => setUsers(data));
  // }, []);

  const onSubmit = (values, { resetForm }) => {
    console.log(values);
    fetch("/signup", {
      method: "POST", // or 'PUT'
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(values),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    resetForm();
  };

  return (
    <>
      <h3>Signup With Username</h3>
      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={onSubmit}
      >
        {({ isSubmitting }) => (
          <Form>
            <div>
              <label htmlFor="name">Name</label>
              <Field type="text" id="name" name="name" />
              <ErrorMessage name="name" component="div" />
            </div>

            <div>
              <label htmlFor="username">Username</label>
              <Field type="text" id="username" name="username" />
              <ErrorMessage name="username" component="div" />
            </div>

            <div>
              <label htmlFor="password">Password</label>
              <Field type="text" id="password" name="password" />
              <ErrorMessage name="password" component="div" />
            </div>

            <button type="submit" disabled={isSubmitting}>
              Submit
            </button>
          </Form>
        )}
      </Formik>
    </>
  );
};

export default Signup;
