# LinkedIn Self-Archive (DMA Portability)

## 📖 Purpose
This project allows you to programmatically extract your **full** personal LinkedIn data using the **Member Data Portability API**.

This API was released by LinkedIn to comply with the EU's **Digital Markets Act (DMA)**. Unlike the standard archive download feature, this tool allows for:
1.  **Granular Access:** Fetch specific data domains on demand (e.g., just your work history or just your messages).
2.  **Automation:** Create scripts to regularly backup your professional history.
3.  **Data Reusability:** Export your profile data into JSON for use in personal websites, resume generators, or data analysis.

---

## ⚙️ LinkedIn API Setup Guide

Setting up this specific API differs from standard LinkedIn apps because it is a **Regulatory Developer Product**.

This API is strictly geo-gated. To use it, your LinkedIn account must be based in:
* **The European Economic Area (EEA)**
* **Switzerland**

### 1. Create a Developer Application
1.  Go to the [LinkedIn Developers Platform](https://www.linkedin.com/developers/).
2.  Click **Create app**.
3.  **Crucial Step:** In the "LinkedIn Page" field, do **not** use your own company page. You must search for and select the specific default page provided by LinkedIn for this purpose:
    * **Search for:** `Member Data Portability (Member) Default Company`
    * *Note: If you link any other page, you will not be able to access the correct API product.*

### 2. Request Product Access
1.  Once your app is created, navigate to the **Products** tab.
2.  Find **Member Data Portability API (Member)**.
    * *Note: Ensure you select the "(Member)" version, not the "(3rd Party)" version.*
3.  Click **Request access** and agree to the terms. Approval is typically automatic.

### 3. Generate Your Access Token
For personal use, you do not need to implement a full OAuth 2.0 login flow. You can manually generate a long-lived token.

1.  In the Developer Portal, go to **Docs and tools** > **OAuth Token Tools**.
2.  Click **Create token**.
3.  Select the **App** you created in Step 1.
4.  Under **Scopes**, select: `r_dma_portability_self_serve` (or `r_dma_portability_member`).
5.  Click **Request access token**.
6.  Log in with your LinkedIn account to authorize the app.
7.  **Copy the Access Token.** This string is your API key.