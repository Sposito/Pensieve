Tipos de Autenticação:
- Baseada em Algo que você sabe
- Baseada em algo que você tem
- Baseado em algo que você é

2FA - Two Factor Authentication
Consiste em usas dois tipos de autenticação para elevar a segurança

SSO - Single Sign On
Através de um login você passa a ter acesso a multiplos serviços. LDAP é o principal protocolo coorporativo

SAML - Security Assertion Mark up language
Padrão aberto que permite compartilhamento de credencias de autorização. um bom exemplo é o Acesso.gov

3 Papéis:
- O principal (Humano): 
- O provedor de Identidade (IDP)
- O provedor de Serviços (SP)

```sequence {theme="hand"}
ServiceProvider <- UserAgent Request Target resource
ServiceProvider <--> UserAgent (Discover the IdP)

```

