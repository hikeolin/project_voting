import React, { useState } from "react";
import { Formik } from "formik";
import * as yup from "yup";
import { Form } from "react-bootstrap";
import LoaderButton from "../components/LoaderButton";
import "./Signup.css";

const initialFields = {
  firstName: "",
  lastName: "",
  email: "",
  password: "",
  passwordConfirm: ""
};

const Schema = yup.object({
  firstName: yup
    .string()
    .required("First Name is required")
    .min(2, "Enter a valid name"),
  lastName: yup
    .string()
    .required("Last Name is required")
    .min(2, "Enter a valid name"),
  email: yup
    .string()
    .email()
    .required("Email is required"),
  password: yup
    .string()
    .required("Password is required")
    .min(4, "Password is invalid"),
  passwordConfirm: yup
    .string()
    .required("Password confirm is required")
    .oneOf([yup.ref("password"), null], "Passwords don't match")
});

export default function SignUp(props) {
  const [isLoading, setIsLoading] = useState(false);

  function handleSubmit(values, ...rest) {
    setIsLoading(true);
    console.log(values);
  }

  return (
    <div className="SignUp">
      <Formik
        onSubmit={handleSubmit}
        initialValues={initialFields}
        validationSchema={Schema}
      >
        {({ handleSubmit, handleChange, values, touched, isValid, errors }) => (
          <Form noValidate onSubmit={handleSubmit}>
            <Form.Group controlId="signup-firstname-id">
              <Form.Label>First Name</Form.Label>
              <Form.Control
                text="text"
                name="firstName"
                value={values.firstName}
                onChange={handleChange}
                isValid={touched.firstName && !errors.firstName}
                isInvalid={!!errors.firstName}
              />
              <Form.Control.Feedback type="valid"></Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                {errors.firstName}
              </Form.Control.Feedback>
            </Form.Group>

            <Form.Group controlId="signup-lastname-id">
              <Form.Label>Last Name</Form.Label>
              <Form.Control
                text="text"
                name="lastName"
                value={values.lastName}
                onChange={handleChange}
                isValid={touched.lastName && !errors.lastName}
                isInvalid={!!errors.lastName}
              />
              <Form.Control.Feedback type="valid"></Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                {errors.lastName}
              </Form.Control.Feedback>
            </Form.Group>

            <Form.Group controlId="signup-email-id">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="text"
                name="email"
                value={values.email}
                onChange={handleChange}
                isValid={touched.email && !errors.email}
                isInvalid={!!errors.email}
              />
              <Form.Control.Feedback type="valid"></Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                {errors.email}
              </Form.Control.Feedback>
            </Form.Group>
            <Form.Group controlId="signup-password-id">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                name="password"
                value={values.password}
                onChange={handleChange}
                isValid={touched.password && !errors.password}
                isInvalid={!!errors.password}
              />
              <Form.Control.Feedback type="valid"></Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                {errors.password}
              </Form.Control.Feedback>
            </Form.Group>
            <Form.Group controlId="signup-passwordConfirm-id">
              <Form.Label>Confirm Password</Form.Label>
              <Form.Control
                type="password"
                name="passwordConfirm"
                value={values.passwordConfirm}
                onChange={handleChange}
                isValid={touched.passwordConfirm && !errors.passwordConfirm}
                isInvalid={!!errors.passwordConfirm}
              />
              <Form.Control.Feedback type="valid"></Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                {errors.passwordConfirm}
              </Form.Control.Feedback>
            </Form.Group>
            <LoaderButton
              block
              variant="secondary"
              type="submit"
              isLoading={isLoading}
              disabled={!isValid}
            >
              {" "}
              Sign Up
            </LoaderButton>
          </Form>
        )}
      </Formik>
    </div>
  );
}
