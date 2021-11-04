import * as React from "react";
import Link from "@mui/material/Link";
import Typography from "@mui/material/Typography";
import { Accordion, AccordionSummary, AccordionDetails } from "./commons";

/**
 * Constructs the react components for the bookmarks page by fetching the locally stored cache and iterating over each item
 * @returns {Components} HTML for constructing the layout of the bookmarks
 */
export default function BookmarkAccordian() {
  const [expanded, setExpanded] = React.useState("bookmark0");
  const rows = getBookmarksFromLocalStorage();
  const handleChange = (panel) => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };


  /**
   * Fetches cache data from chrome storage
   * @returns {Object} contains information about the cached items
   */
  const getBookmarksFromLocalStorage = () => {
    let linksInStorage = JSON.parse(localStorage.getItem("links"));
    return linksInStorage;
  }


  let keys = []
  if (rows)
    keys = Object.keys(rows)

  return (
    <div>
      {keys.map((item, index) => (
        <Accordion key={"bookmark" + index}>
          <AccordionSummary aria-controls={"bookmark" + index + "-content"} id={"bookmark" + index + "-header"}>
            <Typography
              style={{
                marginRight: "auto"
              }}
            >
              {rows[item].question}
            </Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>{rows[item].simple_answer}</Typography>
            <Link color="rgb(30,144,255)" underline="always" target="_blank" rel="noopener" href={item}>
              {"Link"}
            </Link>{" "}
          </AccordionDetails>
        </Accordion>
      ))}
    </div>
  );
}
