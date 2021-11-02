import * as React from 'react';
import axios from "axios"; 
import { styled, createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import MuiDrawer from '@mui/material/Drawer';
import Box from '@mui/material/Box';
import MuiAppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Link from '@mui/material/Link';
import MenuIcon from '@mui/icons-material/Menu';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import CustomizedAccordions from './questions';
import { mainListItems, secondaryListItems } from './listItems';

const result = {
  "results":[
     {
        "question":"What is meant by data preprocessing?",
        "answer":"https://www.analyticsvidhya.com/blog/2021/08/data-preprocessing-in-data-mining-a-hands-on-guide/#:~:text=Data%20preprocessing%20is%20the%20process,learning%20or%20data%20mining%20algorithms."
     },
     {
        "question":"What happens in data preprocessing?",
        "answer":"https://www.techopedia.com/definition/14650/data-preprocessing#:~:text=Data%20preprocessing%20involves%20transforming%20raw,project%20that%20involve%20data%20analyics."
     },
     {
        "question":"What is importance of data preprocessing?",
        "answer":"https://www.sciencedirect.com/topics/engineering/data-preprocessing#:~:text=Data%20preprocessing%20is%20extremely%20important,data%20%5B21%E2%80%9323%5D."
     },
     {
        "question":"What is data preprocessing and why it is important?",
        "answer":"https://www.sciencedirect.com/topics/engineering/data-preprocessing#:~:text=Data%20preprocessing%20is%20an%20important,to%20form%20a%20QSPR%20model.&text=Data%20cleaning%20and%20transformation%20are,used%20to%20create%20a%20model."
     },
     {
        "question":"What is subset selection method?",
        "answer":"https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Subset_Selection_in_Multiple_Regression.pdf"
     },
     {
        "question":"What is subset selection in machine learning?",
        "answer":"https://www.cs.waikato.ac.nz/~ml/publications/1998/Hall-Smith98.pdf"
     },
     {
        "question":"What is best subset selection?",
        "answer":"https://quantifyinghealth.com/best-subset-selection/#:~:text=Best%20subset%20selection%20is%20a,possible%20combinations%20of%20independent%20variables."
     },
     {
        "question":"What is subset selection problem?",
        "answer":"https://home.agh.edu.pl/~wojnicki/phd/node14.html#:~:text=The%20second%20class%20of%20problems,set%20of%20constraints%20is%20satisfied.&text=For%20simplicity%2C%20it%20is%20assumed,is%20both%20discrete%20and%20finite."
     },
     {
        "question":"What is PCA dimensionality reduction?",
        "answer":"https://machinelearningmastery.com/principal-components-analysis-for-dimensionality-reduction-in-python/#:~:text=for%20Dimensionality%20Reduction-,Dimensionality%20Reduction%20and%20PCA,to%20predict%20the%20target%20variable."
     },
     {
        "question":"How PCA is used for dimension reduction?",
        "answer":"https://www.kdnuggets.com/2020/05/dimensionality-reduction-principal-component-analysis.html#:~:text=Principal%20Component%20Analysis(PCA)%20is,of%20orthogonal(perpendicular)%20axes."
     },
     {
        "question":"Is PCA linear dimensionality reduction?",
        "answer":"https://blog.paperspace.com/dimension-reduction-with-principal-component-analysis/#:~:text=Principal%20Component%20Analysis(PCA)%20is,a%20set%20of%20orthogonal%20axes."
     }
  ]
}


function getResults(){
  let results = {}
  axios.get('http://192.168.1.188/results')
      .then(res => {
        results = res.data;
      })
  return results
}

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" underline="none" href="https://mui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const drawerWidth = 240;

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({
    '& .MuiDrawer-paper': {
      position: 'relative',
      whiteSpace: 'nowrap',
      width: drawerWidth,
      transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
      }),
      boxSizing: 'border-box',
      ...(!open && {
        overflowX: 'hidden',
        transition: theme.transitions.create('width', {
          easing: theme.transitions.easing.sharp,
          duration: theme.transitions.duration.leavingScreen,
        }),
        width: theme.spacing(7),
        [theme.breakpoints.up('sm')]: {
          width: theme.spacing(9),
        },
      }),
    },
  }),
);

const mdTheme = createTheme();

function DashboardContent() {
  const [open, setOpen] = React.useState(true);
  const toggleDrawer = () => {
    setOpen(!open);
  };

  return (
    <ThemeProvider theme={mdTheme}>
      <Box sx={{ display: 'flex' }}>
        <CssBaseline />
        <AppBar position="absolute" open={open}>
          <Toolbar
            sx={{
              pr: '24px',
            }}
          >
            <IconButton
              edge="start"
              color="inherit"
              aria-label="open drawer"
              onClick={toggleDrawer}
              sx={{
                marginRight: '36px',
                ...(open && { display: 'none' }),
              }}
            >
              <MenuIcon />
            </IconButton>
            <Typography
              component="h1"
              variant="h6"
              color="inherit"
              noWrap
              sx={{ flexGrow: 1 }}
            >
              Lecture Aid
            </Typography>
          </Toolbar>
        </AppBar>
        <Drawer variant="permanent" open={open}>
          <Toolbar
            sx={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'flex-end',
              px: [1],
            }}
          >
            <IconButton onClick={toggleDrawer}>
              <ChevronLeftIcon />
            </IconButton>
          </Toolbar>
          <Divider />
          <List>{mainListItems}</List>
          <Divider />
          <List>{secondaryListItems}</List>
        </Drawer>
        <Box
          component="main"
          sx={{
            backgroundColor: (theme) =>
              theme.palette.mode === 'light'
                ? theme.palette.grey[100]
                : theme.palette.grey[900],
            flexGrow: 1,
            height: '100vh',
            overflow: 'auto',
          }}
        >
          <Toolbar />
          <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
            <Grid container spacing={3}>
              <Grid item xs={12}>
                <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                  <CustomizedAccordions
                  // results = {getResults()}
                  results = {result}>
                    
                  </CustomizedAccordions>
                </Paper>
              </Grid>
            </Grid>
            {/* <Copyright sx={{ pt: 4 }} /> */}
          </Container>
        </Box>
      </Box>
    </ThemeProvider>
  );
}

export default function Dashboard() {
  return <DashboardContent />;
}