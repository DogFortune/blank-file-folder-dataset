import {
  generateManifest,
} from 'material-icon-theme';

const manifest = generateManifest();
const folderNames = manifest.folderNames
const fileNames = manifest.fileNames
const fileExtensions = manifest.fileExtensions

Bun.write('manifests/folders.json', JSON.stringify(folderNames));
Bun.write('manifests/files.json', JSON.stringify(fileNames));
Bun.write('manifests/extensions.json', JSON.stringify(fileExtensions));
