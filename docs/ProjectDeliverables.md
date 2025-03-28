## Phase 1 - Planning & initial Development
In this phase, our goal was to establish a foundation for our E-Stock inventory tracking system by defining its functionalities, splitting the functions into digestible iterations, and building a base for responsibilities. We aimed to create a clear roadmap for implementation while ensuring that the system meets project requirements.

To achieve this, we:

- Outlined project requirements, focusing on efficient inventory management and role-based access to functions.
- Defined team roles, ensuring clear development, testing, and project management responsibilities.
- Conducted elicitation through research and client meetings to understand system expectations.
- Developed a prioritized feature list, breaking tasks into three iterations in which we will consistently get customer feedback.
- Identified key challenges like data consistency, search accuracy, and secure access control.
- Established team agreements on communication, collaboration, and expected task completion dates.

In short, we created a detailed development plan, ensuring that the next phase will focus on implementing core functionalities by following a set of goals.

## Phase 2 - Minimum Viable Product

In this phase, our goal was to develop a working Minimum Viable Product (MVP) by implementing the major functionalities decided during the planning phase. We prioritized ensuring the system could successfully read inventory data, add, modify products, and search/filter. This phase allowed us to test the core features while identifying areas for improvement.

To achieve this, we:

- Implemented file reading to import inventory data from a CSV file.
- Developed the ability to add new products, including name, price, and stock amount.
- Implemented product editing, though users currently need to update all fields rather than selecting specific ones.
- Enabled search and filtering, allowing searches by name or letter and filtering by stock levels.
- Updated the GitHub repository and Trello board to monitor progress, with structured commits and clear documentation.
- Although we successfully incorporated these features, we identified key limitations that will be addressed in future iterations. The filtering function currently requires users to input all criteria instead of selecting only the necessary filters. 
- The edit function needs refinement to allow users to modify specific product details without overwriting all data.

Moving forward, we will improve user input validation, enhance the filtering system, and introduce a graphical user interface (GUI). We will also expand the inventory data structure to include additional product details, giving users greater control over inventory management.

## Phase 3 - Testing Plan

In this phase, our goal was to design a comprehensive testing plan for the E-Stock system to ensure the core functionalities developed in the MVP (Phase 2) are reliable, robust, and ready for real-world use. This phase focuses on outlining and organizing test strategies that provide full coverage of the system, from individual methods to full user workflows.

To achieve this, we:
- Developed a structured test plan that separates testing into three levels: Unit, Integration, and System tests.
- Categorized test cases based on their scope and purpose — verifying small code units, testing interactions between modules, and validating full user flows.
- Clear Box: Full visibility of internal logic.
- Translucent Box:  focusing on interfaces or data flows.
- Opaque Box: testing from the end-user’s perspective.
- Created test cases using a consistent structure: Each test includes inputs and expected outcomes.
- Mapped tests to system requirements and user stories, ensuring all critical features were tested, including high-risk areas like CSV file operations and edge cases.

Moving forware, we are now ready to proceed confidently into the next development phase. Our focus will shift toward enhancing the user experience, expanding functionality, and refining any weak areas identified through testing.
