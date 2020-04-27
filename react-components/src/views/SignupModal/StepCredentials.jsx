/* eslint-disable */
import React from 'react'
import PropTypes from 'prop-types'

import Services from '@src/Services'
import Field from '@src/components/Field'
import SocialLoginButtons from '@src/components/SocialLoginButtons'

import './stylesheets/StepCredentials.scss'


export default function StepCredentials(props){
  return (
    <div className='great-mvp-signup-wizard-step-credentials'>
      <p className="body-text m-t-0">
         <span>Already have an account? </span><a href={Services.config.loginUrl} id="signup-modal-log-in">Log in</a>
      </p>
      <SocialLoginButtons
        linkedinUrl={props.linkedinLoginUrl}
        googleUrl={props.googleLoginUrl}
      />
      <div className='great-mvp-vertical-separator'>
        <hr/>
        <span>or</span>
        <hr/>
      </div>
      <form onSubmit={event => {event.preventDefault(); props.handleSubmit() }}>
        <Field
          type="text"
          placeholder="Email address"
          name="email"
          disabled={props.disabled}
          value={props.email}
          handleChange={props.handleEmailChange}
          autofocus={true}
          errors={props.errors.email || []}
        />
        <Field
          type="password"
          placeholder="Password"
          name="password"
          disabled={props.disabled}
          value={props.password}
          handleChange={props.handlePasswordChange}
          errors={props.errors.password || []}
        />
        <p className='great-mvp-terms m-0'>By clicking Sign up, you accept the <a href={Services.config.termsUrl} target="_blank" id="signup-modal-t-and-c">terms and conditions</a> of the great.gov.uk service.</p>
        <input
          type="submit"
          value="Sign up"
          id="signup-modal-submit"
          className="great-mvp-wizard-step-submit great-mvp-wizard-step-button m-t-m"
          disabled={props.disabled}
        />
      </form>
    </div>
  )
}

StepCredentials.propTypes = {
  disabled: PropTypes.bool,
  errors: PropTypes.object,
  handlePasswordChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  handleEmailChange: PropTypes.func.isRequired,
  password: PropTypes.string,
  email: PropTypes.string,
  googleUrl: PropTypes.string,
  linkedinUrl: PropTypes.string,
}

StepCredentials.defaultProps = {
  disabled: false,
  errors: {},
  password: '',
  email: '',
}
