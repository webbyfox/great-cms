import React from 'react'

import Enzyme from 'enzyme'
import Adapter from 'enzyme-adapter-react-16'

import SocialLoginButtons from '@src/components/SocialLoginButtons'
import Services from '@src/Services'

Enzyme.configure({ adapter: new Adapter() })

beforeEach(() => {
  jest.useFakeTimers()
})

afterEach(() => {
  Services.setConfig({})
  jest.useRealTimers()
})

test('SocialLoginButtons should render', () => {
  const linkedinUrl = 'http://www.example.com/linkedInUrl/'
  const googleUrl = 'http://www.example.com/google/'

  const component = Enzyme.shallow(
    <SocialLoginButtons
      type="text"
      placeholder="some placeholder"
      name="some-name"
      value="some value"
      handleChange={() => {}}
      linkedinUrl={linkedinUrl}
      googleUrl={googleUrl}
      disabled
      autofocus
    />
  )

  expect(
    component.matchesElement(
      <div>
        <a href={linkedinUrl} className="great-mvp-wizard-step-button m-t-0 m-b-xs">
          <img />
          <span>Continue with LinkedIn</span>
        </a>
        <a href={googleUrl} className="great-mvp-wizard-step-button m-t-0 m-b-xs">
          <img />
          <span>Continue with Google</span>
        </a>
      </div>
    )
  ).toEqual(true)
})
