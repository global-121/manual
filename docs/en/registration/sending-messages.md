---
title: Registrations - Sending messages
hide:
  - toc
---

There is an option to send **outbound messages** via SMS or WhatsApp to registrations for each action you perform in the instance, such as Including, Declining, or Sending payments. If you would like to communicate program progress to the registered individuals, you can turn on **Send a message to registration(s)** and enable messaging through the 121 platform. To enable messaging services, you must create a Twilio account and ensure there are sufficient messaging credits. Contact our team to set this up. Below the steps to follow:

- [Create a Twilio Account](#create-a-twilio-account)
- [Top-up before sending messages](#top-up-before-sending-messages)
- [Formatting phone numbers in Kobo](#formatting-phone-numbers-in-kobo)
- [Send a message to the registered individuals](#send-a-message-to-the-registered-individuals)
- [Custom message](#custom-message)
- [Predefined template messages](#predefined-template-messages)
- [Check the delivery of messages](#check-the-delivery-of-messages)

!!! Important "Who can perform actions in this page?"
    CVA Manager and CVA Officer roles can perform actions in the Registrations page. [Learn more about Roles & Permissions](../users/description-roles.md)

---

### Create a Twilio Account

The 121 Team will assist you in creating your account. If you don't have an account, please contact our team for support. Twilio will prompt you to add a payment method so that funds can be automatically topped up or added as needed.

Once your Twilio account is active, the 121 support team will link it to your 121 platform, enabling the messaging feature.

_Please note that neither 121 nor the Netherlands Red Cross will charge any fees on behalf of Twilio. Our team is solely responsible for the technical integration between the two systems to facilitate message sending._

---

### Top-up before sending messages

You can log in to your Twilio account every time you need to top up your account.

**Sending SMS**
Fees per SMS differ per destination and number of characters sent per messaging. Check the Twilio website for the fees applied to your destination for [SMS](https://www.twilio.com/en-us/sms/pricing/ma).

Note that one **SMS is limited to 160 characters** — messages longer than this will be split into multiple SMS and charged accordingly. For example, a message between 161 and 320 characters will be counted and billed as two SMS. A message between 321 and 481 as three messages, etc. You can use this base to calculate how much your Twilio account should be topped up with. The calculation will include: number of SMS sent x number of registrations x price per SMS for the destination.

**WhatsApp messages**
WhatsApp messages follow a different scheme. You can find the fees description on the [Twilio website](https://www.twilio.com/en-us/whatsapp/pricing).

Once you have calculated the total costs, you can top up your account via the Twilio Portal and add the necessary funds.

!!! Important "Add sufficient funds on your Twilio account"
    Without funds available in your Twilio account, SMS or WhatsApp messages will fail. Contact our team if you need help setting up your Twilio account.

---

### Formatting phone numbers in Kobo

Phone numbers must be entered in international format. This means starting with the country code, followed by the rest of the number without the leading zero. For example, a phone number in the Democratic Republic of Congo (DRC) like 0900887766 should be written as 243900887766 — where 243 is the country code and the initial 0 is removed.

**When building your Kobo form, you can enforce the international phone number format using a constraint or calculation. Kobo does not reformat numbers. The 121 platform removes a leading + or 00 and checks each number with Twilio, but it does not add the country code or remove the leading zero. Numbers that fail this check are rejected with an error. So it's important to configure this logic in your form to ensure consistency.**

| type       | name label         | constraint                | constraint_message                               |
| :--------- | :----------------- | :------------------------ | :----------------------------------------------- |
| text_phone | Enter phone number | regex(., '^243[0-9]{9}$') | Phone must start with 243 and be 12 digits long. |

---

### Send a message to the registered individuals

You can choose to send a message to an individual or multiple selected registrations. You may use either a custom message or a predefined template. See below for the differences and recommended usage guidelines.

### Custom message

In the **Registrations page**:

- Select the list of registrations you want to send a message to;
- Click on the **Message** icon on the top of the page;
- Select **Custom message** and add the message you want to send. The message must have at least 20 characters;
- You can use a variable by using **@** and **selecting the field** you want to insert. Variables allow you to pull information directly from the registration form and insert it automatically, without having to fill it in manually for each person. The content will adjust automatically based on the data provided by each individual during registration;
- Click **Continue to preview** and check the message;
- Click **Send message**. To change the message, click **Go back**.

!!! Important "Custom messages are not translated"
    Custom messages are not automatically translated to the registration's preferred language.

!!! Note "What is a variable and how does it work?"
    A variable is a placeholder that automatically pulls and inserts specific information from your registration form — like a name, email address, phone number, or any other field collected during sign-up.

    You can use a variable by typing @ and selecting the field you want to insert. For example, typing @name will automatically insert each person's name into the message. This means you don’t need to manually customize the message for every individual. The variable will dynamically adjust for each registration, based on the information submitted by that person.

    For example: Dear **@name**, you will receive the amount of **@amount** tomorrow. Kind regards, **@Organization**, would be read as Dear **Paulina Baker**, you will receive the amount of **150 USD** tomorrow. Kind regards, **HelpOrg**.

    *The variables match your Kobo fields and may differ per program.*

### Predefined template messages

If you intend to send messages at various stages of the program, you can add message templates to your instance. To do this, provide the message content along with a title and specify when the message should be triggered. Our support team will set them up. There are 2 options to send templated messages:

1. Templates can be linked to key stages of the program. Some templates are sent automatically, for example when a registration is added to the program or, for some FSPs, when a payment is sent. Templates for Inclusion, Declining and Pausing are proposed in the pop-up when you include, decline or pause registrations: they are only sent if you turn on **Send a message to registration(s)**. Validating registrations does not send a message.

2. Templated messages will be available in the dropdown menu when you click on the **Message** button: select **Template message** and choose the message. You can choose to send them whenever you want, independently of a specific action or stage in the program — unlike the first option, where messages are linked to actions such as registration or inclusion.

---

### Check the delivery of messages

After you send messages, you can check their status in the **Last message status** column of the **Registrations** table.

- If the column is not visible, click **Manage table** (:material-cog:), select **Last message status** and click **Apply**;
- The column shows the type and status of the latest message sent to each registration, for example `sms: delivered` or `whatsapp: failed`. If no message was sent yet, it shows `no messages yet`;
- Filter the column to find, for example, the registrations whose message failed;
- To see all messages of one registration, open the registration profile and go to the **Activity log** tab.

---

-8<- "docs/en/_snippets/contact-support.md"
