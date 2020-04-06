import React, { useState } from 'react';
import { Formik } from 'formik'
import * as yup from 'yup';
import { Form} from 'react-bootstrap';
import LoaderButton from '../components/LoaderButton';
import './Signin.css';

const initialFields = {
    'email': '',
    'password': ''
}

const Schema = yup.object({
    email: yup.string().email()
        .required('Email is required'),
    password: yup.string()
    .min(4,'Password is invalid')
    .required('Password is required')
});

function SignIn(props) {

    const [isLoading, setIsLoading] = useState(false);


    function redirect(history, location){
        const { from } = location.state || { from: { pathname: "/" } };
        history.replace(from.pathname);
    }

    function handleSubmit(values, ...rest){
        setIsLoading(true);
        console.log(values);
        // redirect(props.history, props.location);
    }

    return (
        <div className='SignIn'>
            <Formik
                onSubmit={handleSubmit}
                initialValues={initialFields}
                validationSchema={Schema}
            >
                {({
                handleSubmit,
                handleChange,
                values,
                touched,
                isValid,
                errors}) => (
                        <Form noValidate onSubmit={handleSubmit}>
                            <Form.Group controlId='signin-email-id'>
                                <Form.Label>Email</Form.Label>
                                <Form.Control
                                    type='text'
                                    name='email'
                                    value={values.email}
                                    onChange={handleChange}
                                    isValid={touched.email && !errors.email}
                                    isInvalid={!!errors.email}
                                />
                                <Form.Control.Feedback type='valid'></Form.Control.Feedback>
                                <Form.Control.Feedback type='invalid'>
                                    {errors.email}
                                </Form.Control.Feedback>
                            </Form.Group>
                            <Form.Group controlId='signin-password-id'>
                                <Form.Label>Password</Form.Label>
                                <Form.Control
                                    type='password'
                                    name='password'
                                    value={values.password}
                                    onChange={handleChange}
                                    isValid={touched.password && !errors.password}
                                    isInvalid={!!errors.password}
                                />
                                <Form.Control.Feedback type="invalid">
                                    {errors.password}
                                </Form.Control.Feedback>
                            </Form.Group> 
                            <LoaderButton
                                block
                                variant='secondary'
                                type='submit'
                                isLoading={isLoading}
                                disabled={!isValid}
                            > Log In</LoaderButton>
                        </Form>
                )}
            </Formik>
    </div>
    )
}

export default SignIn;