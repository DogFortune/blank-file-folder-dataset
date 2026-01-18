import {
  generateManifest,
} from 'material-icon-theme';

const manifest = generateManifest();
const folderNames = manifest.folderNames
const fileNames = manifest.fileNames
const fileExtensions = manifest.fileExtensions

Bun.write('manifests/folders.json', JSON.stringify(folderNames, null, 4));
Bun.write('manifests/files.json', JSON.stringify(fileNames, null, 4));
Bun.write('manifests/extensions.json', JSON.stringify(fileExtensions, null, 4));
