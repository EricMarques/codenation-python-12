doc = '''
#%RAML 1.0
title: api-Python12
mediaType: 
  - application/json
baseUri: http://localhost:8081/{version}
version: v1
protocols:
  [HTTP, HTTPS]
securitySchemes:
  JWT:
    type: OAuth 2.0
    description: JWT Token
    describedBy:
      headers:
        Authorization:
          type: string
      responses:
        401:
          description: |
            {"error": "Unauthorized"}
    settings:
      signatures: |
        ["HMAC-SHA256"]

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token : string
        
  Agent:
    type: object
    discriminator: agent_id
    properties:
      agent_id: integer
      name:
        type: string
        maxLength: 50
      status: boolean
      enviroment:
        type: string
        maxLength: 20
      version:
        type: string
        maxLength: 20
      address:
        type: string
        maxLength: 39
      user_id: integer
    example:
      agent_id: 1
      name: CodeNation
      status: true
      enviroment: Python
      version: 1.0.0
      address: 127.0.0.1
      user_id: 1
    
  User:
    type: object
    discriminator: user_id
    properties:
      user_id: integer
      name:
        type: string
        maxLength: 50
      password:
        type: string
        maxLength: 50
      email:
        type: string
        maxLength: 254
      last_login: date-only
      group_id: integer
    example:
      user_id: 1
      name: Eric
      password: CodeNation@123
      email: erc_m@hotmail.com
      last_login: 2020-07-04
      group_id: 1

  Group:
    type: object
    discriminator: group_id
    properties:
      group_id: integer
      name:
        type: string
        maxLength: 20
    example:
      group_id: 1
      name: Devs Python
  
  Event:
    type: object
    discriminator: event_id
    properties:
      event_id:
        type: integer
        required: true
      level:
        type: string
        maxLength: 20
      payload:
        type: string
      shelve:
        type: boolean
      date:
        type: datetime-only
      agent_id:
        type: integer
    example:
      event_id: 1
      level: Event
      payload: Aceleradev Python - CodeNation
      shelve: true
      date: 2020-07-04T22:42:00
      agent_id: 1

/auth/token:
  post:
    description: Create token authentication
    body:
      application/json:
        username: string
        password: string
    responses:
      201:
        body:
          application/json:
            type: Auth
      400:
        body:
          application/json: |
              {"error": "Not found"}
        
/agents:
  get:
    securedBy: JWT
    description: All Agents
    responses:
      200:
        body:
          application/json: Agent[]
  post:
    securedBy: JWT
    description: Create Agent
    body:
      application/json:
        properties:
        example:
          user_id: 1
          name: Python
          status: true
          environment: CodeNation
          version: 1.0.0
          address: 127.0.0.1
    responses:
      201:
        body:
          application/json:
            example:
              agent_id: 1
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
  
  /{id}:
    get:
      securedBy: JWT
      description: Agent detail
      responses:
        200:
          body:
            application/json: Agent
        401: 
          body:
            application/json: |
              {"error": "Unauthorized"}
        404: 
          body:
            application/json: |
              {"error": "Not found"}
    put:
      securedBy: JWT
      description: Update Agent
      responses:
        200: 
          body:
            application/json: Agent
        401: 
          body:
            application/json: |
              {"error": "Unauthorized"}
        404: 
          body:
            application/json: |
              {"error": "Not found"}
    delete:
      securedBy: JWT
      description: Delete Agent
      responses:
        200:
          body:
            application/json: Agent
        401: 
          body:
            application/json: |
              {"error": "Unauthorized"}
        404: 
          body:
            application/json: |
              {"error": "Not found"}
      
  /{id}/events:
    get:
      securedBy: JWT
      description: Get all events by agent_id
      responses:
        200:
          body:
            application/json: Event[]
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
    post:
      securedBy: JWT
      description: Create event to an agent
      body:
        application/json: Event[]
      responses:
        201:
          body:
            application/json: |
              {"message": "Event created"}
        401: 
          body:
            application/json: |
              {"error": "Unauthorized"}
        404: 
          body:
            application/json: |
              {"error": "Not found"}          
    put:
      securedBy: JWT
      description: Update a event by agent_id
      body:
        application/json: Event[]
      responses:
        200:
          body:
            application/json: |
              {"message": "OK"}
        401: 
          body:
            application/json: |
              {"error": "Unauthorized"}
        404: 
          body:
            application/json: |
              {"error": "Not found"}
    delete:
      securedBy: JWT
      description: Delete Event
      body:
        application/json: Event[]
      responses:
        200:
          body:
            application/json: |
              {"message": "OK"}
        401: 
          body:
            application/json: |
              {"error": "Unauthorized"}
        404: 
          body:
            application/json: |
              {"error": "Not found"}

    /{id}:
      get:
        securedBy: JWT
        description: Get event by agent_id and event_id
        body:
          application/json:
        responses:
          200:
            body:
              application/json: |
                {"message": "OK"}
          401: 
            body:
              application/json: |
                {"error": "Unauthorized"}
          404: 
            body:
              application/json: |
                {"error": "Not found"}
      post:
        securedBy: JWT
        description: Create Event
        body:
          application/json:
        responses:
          200:
            body:
              application/json: |
                {"message": "OK"}
          401: 
            body:
              application/json: |
                {"error": "Unauthorized"}
          404: 
            body:
              application/json: |
                {"error": "Not found"}
      put:
        securedBy: JWT
        description: Update event
        body:
          application/json:
        responses:
          200:
            body:
              application/json: |
                {"message": "OK"}
          401: 
            body:
              application/json: |
                {"error": "Unauthorized"}
          404: 
            body:
              application/json: |
                {"error": "Not found"}
      delete:
        securedBy: JWT
        description: Delet Event
        body:
          application/json:
        responses:
          200:
            body:
              application/json: |
                {"message": "OK"}
          401: 
            body:
              application/json: |
                {"error": "Unauthorized"}
          404: 
            body:
              application/json: |
                {"error": "Not found"}
        
/groups:
  get:
    securedBy: JWT
    description: All Groups list
    responses:
          200:
            body:
              application/json: Group[]
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
  post:
    securedBy: JWT
    description: Create Group
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 20
        example:
          name: Dev Python
    responses:
      201:
        body:
          application/json: |
            {"message": "OK"}
      400: 
        body:
          application/json: |
            {"error": "Bad request"}
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
  put:
    securedBy: JWT
    description: Update Group
    responses:
      200:
        body:
          application/json:
  delete:
    securedBy: JWT
    description: Delete Group
    responses:
      200:
        body:
          application/json:

  /{id}:
    get:
      securedBy: JWT
      description: Group detail
      responses:
        200:
          body:
            application/json: Group
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
    put:
      securedBy: JWT
      description: Update Group
      responses:
        200:
          body:
            application/json: |
              {"message": "OK"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
    delete:
      securedBy: JWT
      description: Delete Group
      responses:
        200:
          body:
            application/json: |
              {"message": "OK"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}

/users:
  get:
    securedBy: JWT
    description: All users list
    responses:
      200:
        body:
          application/json: User[]
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
  post:
    securedBy: JWT
    description: Create User
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 50
          password:
            type: string
            maxLength: 50
          email:
            type: string
            maxLength: 254
          last_login:
            type: date-only
        example:
          name: Eric
          password: CodeNation@123
          email: erc_m@hotmail.com
          last_login: 2020-07-04
    responses:
      201:
        body:
          application/json: |
            {"message": "OK"}
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}

  /{id}:
    get:
      securedBy: JWT
      description: Get user by id
      responses:
        200:
          body:
            application/json: User
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
    put:
      securedBy: JWT
      description: Update User
      responses:
        200:
          body:
            application/json: |
              {"message": "OK"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
    delete:
      securedBy: JWT
      description: Delete User
      responses:
        200:
          body:
            application/json: |
              {"message": "OK"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Not found"}
'''