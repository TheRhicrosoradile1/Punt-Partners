# Backend Take Home Assignment

## **Problem Statement**

You are tasked to enhance a SaaS platform providing "Coupon Code" services with a new feature to mitigate fraud using "repeat counts" - the number of times a coupon can be used.

### **Repeat Count Axes:**

- **User Axis**: Specify per User or Global usage.
- **Time Axis**: Define limits per Hour, Day, Week, Month, etc.

### **Required APIs:**

1. **Add Repeat Counts to a Coupon Code**
    - Inputs: Coupon code string, repeat count configuration.
    - Implementations needed:
        - Global Total Repeat Count
        - User Total Repeat Count
        - User Daily Repeat Count
        - User Weekly Repeat Count
    
    ```jsx
    jsxCopy code
    Example Configuration:
    User Total Repeat Count - 3
    User Per Day Repeat Count - 1
    User Per Week Repeat Count - 1
    Global Total Repeat Count - 10000
    
    ```
    
2. **Verify Coupon Code Validity**
    - Ensure existence and adherence to repeat count configurations.
3. **Apply Coupon Code**
    - Validate with Verify Coupon Code API.
    - Update repeat counts accordingly.

## **Deliverables**

- A server implementing the specified APIs.
- Unit tests covering key functionality.
- Source code on GitHub.
- A README file with setup and API testing instructions (e.g., using curl).
- A note discussing trade-offs made and potential scalability challenges.

## **Instructions**

- Focus on object-oriented or functional design principles.
- Ask questions if something is unclear on +919824587433.
- Make assumptions where necessary and document them.
- Prioritise robust error handling.
- Include some tests and outline others you'd write with more time.
- Use an in-memory database abstraction, considering future integration with a persistent store.
- Enjoy the process!

