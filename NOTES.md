# Project Report

## Overview

This document outlines the current status of the project, highlighting completed tasks, pending tasks, and areas for improvement.

## Completed Tasks

1. **GenAI API Integration**:

    - The GenAI API calls have been implemented and tested successfully.
    - Basic functionality of the `/chat` endpoint is operational, though its accuracy can be enhanced.

2. **Non-GenAI API Integration**:
    - Several Non-GenAI API calls have been implemented.
    - Some API calls are pending debugging due to time constraints.

## Pending Tasks

1. **Enhancing Accuracy**:

    - The accuracy of the `/chat` endpoint can be improved further.

2. **Debugging Non-GenAI API Calls**:
    - Several API calls still require debugging and validation.

## Recommendations for Improvement

1. **JWT Token Implementation**:

    - Implement JWT Tokens for authentication during login and registration.
    - Use JWT Tokens for authorization in subsequent API calls instead of relying on usernames.

2. **PDF Storage**:

    - PDFs are currently stored in the local directory `/path`.
    - Consider storing PDFs online for each user to enhance accessibility and organization.

3. **User Management**:
    - Users are currently stored in a list of dictionaries, which is volatile and gets reset upon restarting the application.
    - Implement a persistent user storage solution.
    - A default user ('irish') has been added to streamline testing and avoid repeated registration API calls.

## Code Quality and Documentation

-   **Code Quality**:
    -   The current code quality can be significantly improved with additional time for refactoring and optimization.
-   **Documentation**:
    -   Comprehensive documentation for the codebase is currently lacking and can be improved to facilitate better understanding and maintenance.

## Conclusion

The project has made significant progress, with key functionalities already in place. However, there are several areas that require further development and debugging. Implementing JWT Tokens, enhancing the accuracy of the GenAI API, and improving both code quality and documentation are crucial next steps for completing and refining the application.
