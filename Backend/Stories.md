## User Stories
### **Story 1:**
#### As a user,
#### I want to browse the catalog of books,
#### So that I can see what titles are available for reading.

### **Story 2:**
#### As a user, 
#### I want to type an author and title and click add, 
#### so that I can track what I want to read.

### **Story 3:**
#### As a registered user,
#### I want to mark specific books as my "favorites,"
#### So that I can easily find and access the books I love most in a separate view.

### **Story 4:**
#### As a user,
#### I want to use a navigation bar to switch between different sections of the app,
#### So that I can quickly access the catalog, my favorites, or system statistics.

### **Story 5:**
#### As a store administrator,
#### I want to view real-time data regarding the library's size and user's favourite,
#### So that I can track how the collection is growing and which books are popular.


## Non-Functional Requirements (NFRs)
1. **Performance & UI Responsiveness**
    - **Load Timing:** The main page catalog grid must render completely and become interactive within 2.0 seconds on a standard broadband connection.
    - **API Latency:** The backend endpoints driving the collection updates (e.g., saving favorites or pushing a new book entry) must return responses within 500ms under normal testing workloads.
    - **Smooth Transitions:** Navigating between the "Katalog" and "Statistik" tabs must take less than 200ms, executing without any structural lag or page flickers.

2. **UI Robustness & Translation Resiliency**
    - **DOM Selector Integrity:** The application interface elements must be designed with explicit identifiers (like data-testid) to ensure external translation extensions (e.g., Google Translate injecting <font> tags) do not break layout flows or disconnect automated end-to-end testing hooks.
    - **Cross-Browser Compatibility:** The user interface must scale accurately and execute without functional flaws across all major layout rendering engines: Chromium (Chrome/Edge), WebKit (Safari), and Gecko (Firefox).

3. **Reliability & Data Persistence**
    - **State Persistence:** User preference updates (such as clicking the "heart" button to save a favorite) must reliably persist across manual browser refreshes or view updates.
    - **Graceful Failure handling:** If the backend database fails to load or experiences an API interruption, the frontend must handle the issue gracefully (e.g., showing a static fallback toast message or placeholder text) rather than crashing to a completely blank screen.
   
4. **Security & Data Validation**
    - **Input Injection Defense:** All user text strings entered into forms (such as adding a title or author) must be properly validated and sanitized on both the frontend and backend to secure the app from common Cross-Site Scripting (XSS) or database injection exploits.