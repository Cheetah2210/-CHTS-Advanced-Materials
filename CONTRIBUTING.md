
# Contributing to CHTS-Advanced-Materials

Welcome! We are excited to have you contribute to the Cascading Hybrid Thermal Scavenger project. Because this is a high-performance thermal system licensed under the **CERN OHL v1.2**, we maintain high standards for physical and software integrity.

## 1. Getting Started
* **Check the Issues:** Before starting, look at existing issues to see if there is an active discussion about the module you want to improve.
* **Fork the Repository:** Create your own branch and work within it.
* **Respect the Physics:** Every contribution must align with the `docs/physics_dictionary.md`. If your change introduces new thermal behaviors, please update the dictionary.

## 2. Contribution Workflow
1. **Develop:** Implement your change in a dedicated branch.
2. **Test:** Run all tests in `/tests`. If you are modifying the AI logic, add a new unit test in `tests/Software_validation.md` to ensure your improvement doesn't break the baseline.
3. **Validate:** If your change impacts physical performance, run the protocols in `/validation/protocols` and attach the results to your Pull Request using the `Verification_Report_Template.md`.
4. **Pull Request:** Submit your PR with a clear summary:
    * What physical/code problem are you solving?
    * How does this change impact the Exergy efficiency ($\eta_{ex}$)?
    * Does this change affect the safety/dead-man protocols?

## 3. Code & Design Standards
* **Python Logic:** Follow PEP 8 standards. Ensure your code is modular—keep `observer` logic separate from `data_stream` drivers.
* **Hardware Design:** Export all CAD files as `.STEP` or `.IGES`. Ensure your components include a BOM (Bill of Materials) update.
* **Documentation:** Never commit code without updating the relevant `/docs` file. If you add a new sensor, update the integration matrix.

## 4. License Compliance
This project is licensed under **CERN OHL v1.2**. By contributing, you agree that your modifications will be shared under the same license terms, ensuring this project remains open and accessible for everyone.

---
*Thank you for helping us push the "barest point" of thermodynamic efficiency!*
