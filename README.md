# Mom's Best Friend (Final project)

## M.V.P.
Allow multiple caretakers to record non-vital data (nvd) for a baby. There will
be one primary caretaker who will setup a baby instance and authorize other caretakers
to add baby nvd. Individual categories of nvd can be analyzed quickly via a graph
of the most recent entries. Revenue will be generated via in-app advertising using
the Amazon Product Advertising API.

## Milestones
1. Create a caretaker account/login and add a baby
2. Add an event, display events
3. Graphing functionality
4. Add a secondary caretaker
5. In-app advertising

## Elevator pitch
Mom's Best Friend is an app for keeping track of all of a baby's important information.
For mothers who are tired of recording their baby's information with paper and pen,
they can now record all their baby's information easily with their smartphone. This
gives them easy access to all their baby's information with charts that make it easy to spot
trends in their baby's behavior. What sets Mom's Best Friend apart from other baby
apps is the ability for many caretakers to add to a baby's information. This is a
must have feature for mom's who have others help care for their baby and still want
a consistent record of their baby's information.



## Personas
### Jennifer Thomas
- Photo: http://midlifemaverick.com/wp-content/uploads/2012/08/Molly-Mahar.jpg
- Education: Four year degree, will return for masters degree after the child is born.
- Household: Lives in a house with husband (Mike), just celebrated their 3rd wedding
             anniversary. They have a dog and are expecting their first child. Her
             parents live in town and will be helping with their second grandchild.
- Hobbies: Jogging, Cooking, and Crafting
- Tech-savvy: False. Upgrades her phone at her contract renewal date.
- Social media usage: Moderate. Checks/posts to Facebook and Instagram several times daily.
- Baby preparation: Has read several parenting books, and has asked friends and
                    family members for advice on how to be prepared. Prepared a
                    detailed list of items for her baby shower and purchased all
                    items not received at the shower.
- Baby care: Plans to take the maximum amount of time off of work to be with her
             new baby. Will use a combination of day-care, parents, and friends
             for care after returning to work.
- Income level: $80-100K (dual)

### Amy Rosas
- Photo: https://cdn3.nursinglicensemap.com/content/9d3968d2dc1b4bdeb09b74e20999ade4/Registered_nurse.jpg
- Education: Four year degree.
- Household: Lives alone in an apartment. Has a cat.
- Hobbies: Watching TV.
- Tech-savvy: False. Shares a plan with a friend. Buys the affordable phone model
              off contract.
- Social media usage: Moderate. Checks/posts to Facebook and Instagram several times daily.
- Baby preparation: Has a family member with children that she consults for advice.
- Baby care: Plans to take two weeks off of work to be with her new baby. Will
             use a combination of day-care and friends for care after returning to work.
- Income level: $40-60K (single)

## User stories
- As a mother I want to record the time my baby went to sleep so that the nanny may know how long the baby has been asleep.
- As a nanny I want to record how much milk the baby drank so that the mother will know how well the child ate.
- As a mother I want to add caretakers to my baby's account so that they can record the baby's events.
- As a caretaker I want to accept an invitation to a baby's account so that I can edit the records.
- As a mother I want to be able to customize my baby's chart so that I only see relevent information to my childcare style.
- As a caretaker I want to be able to see a visualization of the data for a specific catagorie so that I can be updated about the baby quickly.

## Interviews
- Lisa A. - Childcare professional with nearly two decades of experience providing
both in home and facility day-care. Lisa felt that it would be more convenient to
record infant nvd using her smartphone, rather than using the current system of
paper and pen. She finds that tracking down the paper to record the information
is somewhat painstaking and time consuming. She felt that if she could simply
use her phone to enter the information, that would make her job a little easier.
She felt that this product will be useful in both home and facility day care
settings, as the facility day care that she works at still uses paper and pen to
record infant nvd. The only problem that she could identify in using the product
was the related to the technology willingness of the users. She stated that some
of the "dinosaurs" that she works with wouldn't know how to use their phones to
utilize the application. She did note that she would rather pay for the application
instead of having in-app advertising.

- Michelle T. - Physician and mother of 2 year old twin girls. Michelle works
part-time and relys on a combination of in home day-care and family to provide
care to her children while at work. While her children were infants she discovered
that she needed a way to allow multiple caretakers to record nvd for her children
and allow all to have access to that data at any time. The only solution that she
could find to solve this problem was to utilize a paper and pen based spreadsheet.
She feels like having a smartphone app that could replace the paper spreadsheet
would be nice because she could monitor what was happening while at work. She would
also find it useful to be able to see a graph of the data so she could quickly identify
trends in behavior. This was a feature that was available in other baby record apps,
unfortunately they did not allow for multiple users and thus were not useful to her.
The only problem that she could identify was related to users not entering data.   

## Data models
- Baby (has one family)
  - first name (str)
  - last name (str)
  - birthdate (DateField)
- Event (has one baby)
    - date and time (DateTimeField)
  - breast fed
    - breast (choice: left, right)
  - bottle fed
    - amount (int)
  - diaper
    - status (choice: wet, bm)
  - temperature
    - temp (int)
  - medication
    - type (str)
  - sleep
    - (time)
  - awake
    - (time)
- Caretaker (has one family)
  - first name (str)
  - last name (str)
  - email (EmailField)
  - phone number (PhoneNumberField)
  - relationship to baby (choice: parent, family, friend, nanny)
- Family (has many cartaker's & baby's)
  - name (str)
