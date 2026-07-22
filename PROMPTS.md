**1. Initial Project Setup**

Prompt: "I have this project set up. Please walk me through a step-by-step process to build it with clean, minimal code suitable for a beginner. Also let me know when I should commit at each stage, based on what the project requirements specify."

Used for: Getting a step-by-step build plan for the FastAPI + React project matching the kata requirements, including exactly when to commit and how to format TDD-style commit messages with AI co-author trailers.

**2. Fixing pytest fixture errors**

Prompt: "I'm getting a 'fixture client not found' error when running pytest. Here's the full error output — can you help me fix it?"

Prompt: "Now I'm getting a ModuleNotFoundError: No module named 'app'. Here's the traceback."

Used for: Debugging why pytest couldn't find the client fixture (missing conftest.py) and why it then couldn't import app (missing pythonpath config). Added conftest.py with a TestClient fixture using an isolated test database, and a pytest.ini to fix the import path.

**3. Fixing the frontend "npm run dev" error**

Prompt: "I'm getting an npm ENOENT error saying it can't find package.json when I run npm run dev. Here's the error output."

Used for: Diagnosing that the command was being run from the wrong directory (project root instead of frontend/).

**4. Debugging login/register failures**

Prompt: "Both login and registration are failing on the frontend. Here's my main.py with the CORS configuration."

Prompt: "Here's a screenshot of the login error, along with the backend log showing the frontend is running on port 3000."

Used for: Diagnosing a CORS mismatch — the backend only allowed localhost:5173, but the frontend was actually running on localhost:3000. Fixed by updating allow_origins in CORSMiddleware.

**5. Checking project completeness against the kata specification**

Prompt: "Does this project fulfill all the requirements I gave you?"

Prompt: "Can you check whether my project is complete based on this specification?" (full kata document attached)

Prompt: "I've uploaded the project as a zip file — please review the actual code."

Used for: Asking Claude to inspect the actual uploaded project (backend routes, models, frontend) against the original kata requirements. This surfaced a critical gap: none of the vehicle endpoints had authentication or admin checks, despite the spec requiring "Protected" routes and "Admin only" restrictions on delete/restock.

**6. Adding authentication and authorization to vehicle endpoints**

Prompt: "Is adding auth/admin protection to the vehicle endpoints actually necessary, or optional?"

Used for: Understanding why backend-enforced authorization matters (hiding buttons on the frontend is not real security), and implementing get_current_user and require_admin dependency functions in security.py, then wiring them into every route in main.py — all vehicle routes require login, and delete/restock require admin privileges.

**7. Styling — color theme iterations**

Prompt: "I'd like to change the color scheme of the frontend. How should I approach this?"

Prompt: "I'd like the site to look professional."

Prompt: "Can you show me a preview of how this will actually look before I apply it?"

Prompt: "I'd like a black-and-white or light theme instead — something clean that will make a strong impression in a job application."

Prompt: "The black is too heavy — please use a lighter grey wherever a solid black background is currently used."

Prompt: "Here's a screenshot of one component — where in the code do I change this specific color to grey?"

Used for: Iterating on the app's color scheme — first a slate/indigo "professional" palette, then a full black-and-white minimal theme, then softened to a lighter grey palette based on feedback that solid black blocks felt too heavy. This included building an HTML preview to visualize changes before editing the real React files, and providing exact before/after Tailwind class diffs per file.

**8. Admin vs. User role-based access control**

Prompt: "Should the admin and regular user have completely separate pages, or should the same page just hide the Restock and Delete buttons for regular users?"

Prompt: "It's not clear from the UI whether I'm logged in as admin or as a regular user — also, should the login page let me choose to log in as either role?"

Prompt: "What about the admin's view specifically — how do I test that?"

Prompt: "To confirm my understanding: should the system check if the email address contains 'admin' to decide whether to show the admin view?"

Prompt: "Can you walk me through exactly how to set this up and test it end-to-end?"

Used for:

Deciding on the correct pattern: a single dashboard with admin-only controls conditionally rendered based on an is_admin flag, rather than separate pages — and clarifying that role should never be selectable at login, since that would be a security flaw.
Wiring is_admin through the login API response, localStorage, and down through Dashboard → VehicleList → VehicleCard.
Adding a visible Admin/User role badge in the navbar for clarity while testing.
Clarifying that role must be determined by a database flag, never by inspecting the email address itself.
Writing a seed_admin.py script to create a ready-made test admin account, since the registration endpoint intentionally never allows a user to self-register as admin.
Identifying and fixing a bug where an earlier edit had silently failed to correctly pass the isAdmin prop through the component tree, verified by re-reading the files and confirming the fix worked end-to-end.
