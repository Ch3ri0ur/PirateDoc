# License Information

Only a short Complication of the most used Licenses and some Important Information about Copyright and Copyleft.

This is only a short Summary, more Information can be found in the Linked Sources.

This is no Legal Advice!!!, only a small overview!!!

## Copyright

Copyright isn't a License, it's about who owns/created the software code (intellectual property) and can decide about distribution and right to copy. A Copyright holder can give permission to others to use it or transfer the Copyright Ownership.
A Copyright always exists, even if the Author didn't add an Copyright Quote.

The Owner of the Copyright can give others permission to use the code by adding a Quote, there they allow others to do it.
Legal documents for giving someone the right to contribute are Contributor License Agreement (CLA) and to transfer ownership of the copyright are Copyright Assignment Agreement (CAA).

Most License for OpenSource Software or Free Software force the Owner to allow others of getting free Copy of Sourcecode to study or modify. This doesn't mean that the Code looses its copyright or is free of charge to use.

A Copyright Quote mustn't be removed or modified! It is usually acceptable to move the Quote to a more Central location or when a file gets split up, to duplicate it in each file.

When someone else modifies a work (with allowance) the new code and changes fall under a new copyright with the modifier as owner. This doesn't mean that the old copyright is replaced, but that all changes are protected by an new one. 
A Copyright Quote for the Modification can be added to the file/section or listed under the original Copyright Quote with or without a description what changes have been introduced. In versioning tools all changes get tracked and it can be easily seen who did which changes. Adding a Date/Year to the copyright helps to keep track.
The Copyrights can be combined if the owner of the original work allows it to become a combined work, but often it will stay a separate copyright for the modified/added work with the new author as owner. This means this modified work now needs the agreement of all the owners of the existing copyrights to be distributed and copied. Partial Copy or Distribution of only code that is under copyright of one owner would of course only need the one owners agreement.

There are two maintaining methods for maintaining copyright notices.

- File-scope copyright notices mean the copyright is managed for every File. This way its much easier to see which Copyrights exist for the code in the file, but is also makes it much harder to track everything and keep it up to data.
- Centralized copyright notices gets managed in one file in the top level of the Project. The copyright quote should be updated with specific information about the work each contributor did. This hasn't to be done and in versioning tools like Github it is easy to track down which Code is made by who.

If all Codeparts/intellectual Property of an Copyright Owner have been replaced/removed, than the copyright quote of this person can be removed. But it is very difficult to be sure and often you still need to credit the creator for the idea or inspiration. 

https://softwarefreedom.org/resources/2012/ManagingCopyrightInformation.html
https://opensource.org/faq#:~:text=As%20long%20as%20you%20own,give%20it%20to%20somebody%20else!
https://en.wikipedia.org/wiki/Copyright

## Copyleft

Copyleft is a rule that shall prevent others to redistributed the program (with or without modification) with a restrictions on the central freedom of free Software. This means a project that inherits/includes a project with a copyleft rule needs to contain this rule from now in ist onw rules. 

Many OpenSource Licenses come with a Copyleft rule included, which is for protecting the project to become closed source, taking away the freedom of free software and not crediting the work of the original authors.

https://www.gnu.org/philosophy/free-sw.en.html


## Free Software

Free Software is defined by The Free Software Foundation (FSF). Programms under a Free Software License have to follow the rules of Freedom, which allow the user to run, study or modify the code and retribute it to others. This doesn't need to be free of charge, but an option needs to be provided to the user.

- Freedom to run means you don't have to communicate to the developer for what you want to use it.
- Freedom to study and modify the SourceCode means a way to access the SourceCode needs to be given any you are free to do changes.
- Freedom to redistribute the software without or with own changes, without needing to notify, ask or pay someone. But a license of free software can permit other ways of releasing/contributing it.
- This doesn't mean that you don't have to pay for obtaining a copy of the Program/Executable or SourceCode.

Software released unter a free software license needs to follow the rules a both.

https://www.fsf.org/
https://www.gnu.org/philosophy/free-sw.en.html
https://en.wikipedia.org/wiki/Free_software

## Open Source

Open Source isn't equal to Free Software and is defined by the Open Source Initiative. Open Source comes with more restriction than Free Software, but Free Software is more strict defined and more focused on the Freedom for the user. Because of the Similarity do Programms with a License that follows OpenSource or FreeSoftware rules often fulfill both definitions.

https://opensource.org/osd
https://en.wikipedia.org/wiki/Open_source
https://www.gnu.org/philosophy/open-source-misses-the-point.en.html
https://www.gnu.org/philosophy/free-sw.en.html


## GNU General Public License

GNU General Public License is a License provided by Free Software Foundation, Inc. This License is free of Charge and can be use for own Project that should follow the rules of Free Software. This License includes a Copyleft restriction that prevents others from using the project in own Projects that have closed Source or other restriction against Free Software.

The latest Version of this License is GNU GPL v3.

The GNU Lesser General Public License contains a less strong Copyleft.

https://www.gnu.org/licenses/quick-guide-gplv3.en.html
https://www.gnu.org/licenses/licenses.en.html
https://www.gnu.org/philosophy/free-sw.en.html

## GNU Affero GPL

The GNU Affero General Public License is a GNU GPL v3 with the addition of closing a loophole. The definition of the regular GNU GPL was that the freedoms only have to be applied when distributing the modified software. The new restriction forces that it also has to follow the rules of freedom if a modified Version is used to run a service others can use.

https://www.gnu.org/licenses/why-affero-gpl.en.html

## MIT License

Is a permissive free software license created by the Massachusetts Institute of Technology (MIT). This license has only minimal restrictions on how to use, modify, merge or redistribute and doesn't include a copyleft rule. But the copies or substantial portions of the Software need to include a copy of the terms of the MIT License and of the copyright notices.

https://en.wikipedia.org/wiki/MIT_License
https://opensource.org/licenses/MIT
https://en.wikipedia.org/wiki/Permissive_software_license

## APACHE License

The APACHE License is very similar to the MIT License and was created by Apache Software Foundation (ASF). It is also a permissive free software license with no copyleft and allows modified work to be published under an different License. But all unmodified parts need to stay under the old (APACHE2) License.

The currently public provided License from Apache Software Foundation is APACHE LICENSE, VERSION 2.0.

https://www.apache.org/licenses/LICENSE-2.0
https://en.wikipedia.org/wiki/Apache_License